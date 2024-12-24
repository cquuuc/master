import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# 设置随机种子以便复现
np.random.seed(42)

# 模拟参数
num_samples = 1000
fault_type = "放电故障"
fault_positions = ["上部", "中部", "下部"]
energy_conversion_rate = np.random.uniform(
    0.5, 1.5, num_samples
)  # 能量转化系数，范围在0.5到1.5之间

# 生成传感器数据
current = np.random.normal(50, 5, num_samples)  # 电流 (A)
voltage = np.random.normal(220, 10, num_samples)  # 电压 (V)
temperature = np.random.normal(70, 5, num_samples)  # 温度 (°C)
pressure = np.random.normal(0.1, 0.01, num_samples)  # 初始压力 (MPa)

# 计算压力变化
pressure_increase_upper = 0.06 * (energy_conversion_rate - 1)  # 升高座内压力变化 (MPa)
pressure_increase_tank = 0.01 * (energy_conversion_rate - 1)  # 油箱内压力变化 (MPa)

# 随机选择故障位置
fault_locations = np.random.choice(fault_positions, num_samples)

# 创建DataFrame
data = pd.DataFrame(
    {
        "故障类型": [fault_type] * num_samples,
        "故障位置": fault_locations,
        "能量转化系数": energy_conversion_rate,
        "电流(A)": current,
        "电压(V)": voltage,
        "温度(°C)": temperature,
        "初始压力(MPa)": pressure,
        "升高座内压力变化(MPa)": pressure_increase_upper,
        "油箱内压力变化(MPa)": pressure_increase_tank,
    }
)

# 计算总压力变化
data["总压力变化(MPa)"] = data["升高座内压力变化(MPa)"] + data["油箱内压力变化(MPa)"]

# 数据预处理
X = data[["能量转化系数", "电流(A)", "电压(V)", "温度(°C)", "初始压力(MPa)"]]
y = data["总压力变化(MPa)"]

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 特征标准化
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 构建神经网络模型
model = Sequential()
model.add(Dense(20, input_dim=X_train.shape[1], activation="relu"))  # 输入层
model.add(Dense(10, activation="relu"))  # 隐藏层
model.add(Dense(1))  # 输出层

# 编译模型
model.compile(optimizer="adam", loss="mean_squared_error")

# 训练模型
model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=0)

# 预测
y_pred = model.predict(X_test)

# 可视化结果
plt.figure(figsize=(12, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot(
    [y_test.min(), y_test.max()], [y_test.min(), y_test.max()], "r--", lw=2
)  # 参考线
plt.title("神经网络预测总压力变化")
plt.xlabel("真实值 (MPa)")
plt.ylabel("预测值 (MPa)")
plt.grid()
plt.show()

# 输出部分预测结果
predicted_data = pd.DataFrame({"真实值": y_test, "预测值": y_pred.flatten()})
print(predicted_data.head())
