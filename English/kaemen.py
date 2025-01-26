import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from filterpy.kalman import KalmanFilter
from sklearn.metrics import mean_squared_error

# 读取数据
stab_data = pd.read_csv(
    r"/kaggle/input/smart-grid-stability/smart_grid_stability_augmented.csv"
)
stab_data.dropna(inplace=True)  # 删除缺失值

# 将稳定性标签映射为数字
map1 = {"unstable": 0, "stable": 1}
stab_data["stabf"] = stab_data["stabf"].replace(map1)

# 划分特征和标签
X = stab_data.drop("stabf", axis=1)
y = stab_data["stabf"]

# 使用train_test_split划分数据集
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 特征标准化
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 1. 使用卡尔曼滤波器平滑数据
kf = KalmanFilter(dim_x=2, dim_z=1)  # 创建卡尔曼滤波器
kf.x = np.array([X_train[0, 0], 0])  # 初始状态
kf.F = np.array([[1, 1], [0, 1]])  # 状态转移矩阵
kf.H = np.array([[1, 0]])  # 观测矩阵
kf.P *= 1000.0  # 协方差矩阵
kf.R = 5  # 测量噪声
kf.Q = np.array([[1, 0], [0, 3]])  # 过程噪声

# 对训练数据应用卡尔曼滤波
filtered_data = []
for z in X_train[:, 0]:  # 假设我们只对第一列特征进行滤波
    kf.predict()
    kf.update(z)
    filtered_data.append(kf.x[0])  # 记录滤波后的值

filtered_data = np.array(filtered_data)

# 2. 使用ARIMA模型进行时间序列预测
# 拟合ARIMA模型
model = ARIMA(filtered_data, order=(5, 1, 0))  # 选择合适的(p, d, q)参数
model_fit = model.fit()

# 进行预测
forecast = model_fit.forecast(steps=len(X_test))
forecast = pd.Series(forecast, index=y_test.index)

# 3. 评估模型
# 计算均方误差
mse = mean_squared_error(y_test, forecast)
print(f"Mean Squared Error: {mse}")

# 绘制预测结果与实际值对比
plt.figure(figsize=(14, 6))
plt.plot(y_test.index, y_test, label="实际值", color="blue")
plt.plot(forecast.index, forecast, label="预测值", color="orange")
plt.title("ARIMA预测与实际值对比")
plt.xlabel("时间")
plt.ylabel("稳定性")
plt.legend()
plt.show()
