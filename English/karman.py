import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import MinMaxScaler
from matplotlib import font_manager
from statsmodels.tsa.stattools import adfuller as ADF

# 设置字体为支持中文的字体
font_path = "C:/Windows/Fonts/simsun.ttc"  # 确保路径正确
font_prop = font_manager.FontProperties(fname=font_path)
plt.rcParams["font.family"] = font_prop.get_name()

# 读取CSV文件并将'report_date'列解析为日期
user_balance = pd.read_csv(
    "user_balance_table.csv", parse_dates=["report_date"], index_col="report_date"
)

# 按照报告日期分组并计算总购买金额
df = user_balance.groupby(["report_date"])["total_purchase_amt"].sum()
purchase_seq = pd.Series(df, name="value")

# 差分处理
purchase_seq_diff = purchase_seq.diff().dropna()

# ADF检验
adf_result = ADF(purchase_seq_diff)
print("差分序列 ADF 检验结果: ", adf_result)

# 划分训练集和测试集
purchase_seq_train = purchase_seq_diff["2014-04-01":"2014-07-31"]
purchase_seq_test = purchase_seq_diff["2014-08-01":"2014-08-10"]

# 数据归一化
scaler = MinMaxScaler()
purchase_seq_train_scaled = scaler.fit_transform(
    purchase_seq_train.values.reshape(-1, 1)
)

# 可视化原始数据
plt.figure(figsize=(12, 6))
plt.plot(purchase_seq, label="总购买金额", color="blue")
plt.xlabel("日期")
plt.ylabel("金额")
plt.title("余额宝总购买金额时间序列")
plt.legend()
plt.grid()
plt.show()

# ARIMA建模
arima_model = ARIMA(purchase_seq_train, order=(5, 1, 1))  # 选择合适的(p, d, q)
arima_fit = arima_model.fit()
# 获取AIC和BIC
arima_aic = arima_fit.aic
arima_bic = arima_fit.bic
print(f"ARIMA模型 AIC: {arima_aic}, BIC: {arima_bic}")
arima_forecast = arima_fit.forecast(steps=len(purchase_seq_test))  # 预测测试集长度


# LSTM建模
# 数据预处理
def create_dataset(data, time_step=1):
    X, Y = [], []
    for i in range(len(data) - time_step):
        a = data[i : (i + time_step)]
        X.append(a)
        Y.append(data[i + time_step])
    return np.array(X), np.array(Y)


# 准备LSTM输入数据
time_step = 10
data_values = purchase_seq_train_scaled.flatten()  # 扁平化数据
X, Y = create_dataset(data_values, time_step)
X = X.reshape(X.shape[0], X.shape[1], 1)  # LSTM输入格式

# 构建LSTM模型
lstm_model = Sequential()
lstm_model.add(
    LSTM(20, return_sequences=True, input_shape=(X.shape[1], 1))
)  # 减少单元数
lstm_model.add(LSTM(20))
lstm_model.add(Dense(1))
lstm_model.compile(optimizer="adam", loss="mean_squared_error")

# 训练LSTM模型
early_stopping = EarlyStopping(monitor="loss", patience=10)  # 添加早停回调
lstm_model.fit(X, Y, epochs=100, batch_size=32, callbacks=[early_stopping])

# 准备测试集的输入数据
last_train_data = purchase_seq_train_scaled[-time_step:]  # 使用归一化后的数据
X_test = np.array([last_train_data])
X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)  # LSTM输入格式

# LSTM预测
lstm_forecast = []
for _ in range(len(purchase_seq_test)):
    prediction = lstm_model.predict(X_test)
    lstm_forecast.append(prediction[0, 0])
    # 更新X_test为最新的输入
    X_test = np.concatenate((X_test[:, 1:, :], prediction.reshape(1, 1, 1)), axis=1)

# 反归一化预测结果
lstm_forecast = scaler.inverse_transform(
    np.array(lstm_forecast).reshape(-1, 1)
).flatten()


# 动态加权平均
def dynamic_weighted_average(arima_preds, lstm_preds, measurements):
    n = len(arima_preds)
    weights_arima = np.zeros(n)
    weights_lstm = np.zeros(n)

    # 初始权重
    weights_arima[0] = 0.5
    weights_lstm[0] = 0.5

    # 卡尔曼滤波参数
    Q = 1e-3  # 过程噪声协方差
    R = 0.01  # 观测噪声协方差
    P_arima = 1.0  # ARIMA的估计误差协方差
    P_lstm = 1.0  # LSTM的估计误差协方差

    for k in range(1, n):
        # 计算预测误差
        error_arima = measurements[k] - arima_preds[k - 1]
        error_lstm = measurements[k] - lstm_preds[k - 1]

        # 更新卡尔曼增益
        K_arima = P_arima / (P_arima + R)
        K_lstm = P_lstm / (P_lstm + R)

        # 更新权重
        weights_arima[k] = weights_arima[k - 1] + K_arima * error_arima
        weights_lstm[k] = weights_lstm[k - 1] + K_lstm * error_lstm

        # 归一化权重
        total_weight = weights_arima[k] + weights_lstm[k]
        weights_arima[k] /= total_weight
        weights_lstm[k] /= total_weight

        # 更新估计误差协方差
        P_arima = (1 - K_arima) * P_arima + Q
        P_lstm = (1 - K_lstm) * P_lstm + Q

    # 组合预测
    combined_forecast = weights_arima * arima_preds + weights_lstm * lstm_preds
    return combined_forecast


def adaptive_kalman_filter(arima_preds, lstm_preds, measurements):
    n = len(arima_preds)
    weights_arima = np.zeros(n)
    weights_lstm = np.zeros(n)

    # 初始权重
    weights_arima[0] = 0.5
    weights_lstm[0] = 0.5

    # 卡尔曼滤波参数
    Q = 1e-5  # 过程噪声协方差
    R = 0.1  # 观测噪声协方差
    P_arima = 1.0  # ARIMA的估计误差协方差
    P_lstm = 1.0  # LSTM的估计误差协方差

    for k in range(1, n):
        # 计算预测误差
        error_arima = measurements[k] - arima_preds[k - 1]
        error_lstm = measurements[k] - lstm_preds[k - 1]

        # 更新卡尔曼增益
        K_arima = P_arima / (P_arima + R)
        K_lstm = P_lstm / (P_lstm + R)

        # 更新权重
        weights_arima[k] = weights_arima[k - 1] + K_arima * error_arima
        weights_lstm[k] = weights_lstm[k - 1] + K_lstm * error_lstm

        # 归一化权重
        total_weight = weights_arima[k] + weights_lstm[k]
        weights_arima[k] /= total_weight
        weights_lstm[k] /= total_weight

        # 更新估计误差协方差
        P_arima = (1 - K_arima) * P_arima + Q
        P_lstm = (1 - K_lstm) * P_lstm + Q

        # 自适应调整 Q 和 R
        Q = 1e-5 + 0.1 * np.abs(error_arima)  # 根据 ARIMA 的误差动态调整 Q
        R = 0.1 + 0.1 * np.abs(error_lstm)  # 根据 LSTM 的误差动态调整 R

    # 组合预测
    combined_forecast = weights_arima * arima_preds + weights_lstm * lstm_preds
    return combined_forecast


# 使用动态加权平均
combined_forecast_no_kalman = dynamic_weighted_average(
    arima_forecast, lstm_forecast, purchase_seq_test.values
)

# 使用自适应卡尔曼滤波
combined_forecast_kalman = adaptive_kalman_filter(
    arima_forecast, lstm_forecast, purchase_seq_test.values
)

# 绘制结果
plt.figure(figsize=(12, 6))
plt.plot(
    purchase_seq_test.index,
    purchase_seq_test.values,
    label="真实购买金额",
    color="g",
)
plt.plot(
    purchase_seq_test.index,
    arima_forecast,
    label="ARIMA预测",
    color="b",
)
plt.plot(
    purchase_seq_test.index,
    lstm_forecast,
    label="LSTM预测",
    color="r",
)
plt.plot(
    purchase_seq_test.index,
    combined_forecast_no_kalman,
    label="动态加权平均预测（无卡尔曼滤波）",
    color="orange",
)
plt.plot(
    purchase_seq_test.index,
    combined_forecast_kalman,
    label="动态加权平均预测（有卡尔曼滤波）",
    color="purple",
)
plt.xlabel("时间")
plt.ylabel("金额")
plt.title("余额宝申购金额预测对比")
plt.legend()
plt.grid()
plt.show()
