# 导入必要的库
import pandas as pd  # 用于数据处理
import matplotlib.pyplot as plt  # 用于数据可视化
import seaborn as sns  # 用于更美观的数据可视化
import numpy as np  # 用于数值计算
from sklearn.model_selection import train_test_split  # 用于数据集划分
from sklearn.preprocessing import StandardScaler  # 用于特征标准化
from tensorflow.keras.models import Sequential  # 用于构建神经网络模型
from tensorflow.keras.layers import Dense, Dropout  # 用于构建神经网络的层
from tensorflow.keras.optimizers import Adam  # 优化器
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    confusion_matrix,
)  # 用于模型评估
from datetime import datetime  # 用于时间处理
from tensorflow.keras.models import load_model  # 用于加载已保存的模型

# 检查输入数据文件
import os

for dirname, _, filenames in os.walk("/kaggle/input"):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# 数据读取
start_time = datetime.now()  # 记录开始时间
stab_data = pd.read_csv(
    r"/kaggle/input/smart-grid-stability/smart_grid_stability_augmented.csv"
)  # 读取数据集

# 显示数据的前几行和后几行
print(stab_data.head())
print(stab_data.tail())
print(stab_data.isna().sum())  # 检查缺失值

# 特征相关性探索
map1 = {"unstable": 0, "stable": 1}  # 将稳定性标签映射为数字
stab_data["stabf"] = stab_data["stabf"].replace(map1)  # 替换标签
stab_data["stabf"].value_counts(normalize=True)  # 计算每个类别的比例

# 计算相关性矩阵并可视化
correlation_matrix = stab_data.corr()  # 计算相关性矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)  # 绘制热图
plt.title("Correlation Map")  # 设置标题
plt.show()  # 显示图形

stab_data.drop("stab", axis=1, inplace=True)  # 删除不需要的列

# 划分训练集和测试集
X = stab_data.drop("stabf", axis=1)  # 特征
y = stab_data["stabf"]  # 标签

# 使用train_test_split划分数据集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 将数据转换为numpy数组
X_train = X_train.values
y_train = y_train.values
X_test = X_test.values
y_test = y_test.values

# 特征标准化
scaler = StandardScaler()  # 创建标准化对象
X_train = scaler.fit_transform(X_train)  # 拟合并转换训练数据
X_test = scaler.transform(X_test)  # 仅转换测试数据

# 构建ANN模型
model = Sequential(
    [  # 创建顺序模型
        Dense(64, activation="relu", input_dim=X_train.shape[1]),  # 输入层
        Dropout(0.3),  # Dropout层用于正则化
        Dense(32, activation="relu"),  # 隐藏层
        Dropout(0.3),  # Dropout层用于正则化
        Dense(1, activation="sigmoid"),  # 输出层，二分类
    ]
)

model.summary()  # 打印模型摘要

# 编译模型
model.compile(
    optimizer=Adam(learning_rate=0.001),  # 使用Adam优化器
    loss="binary_crossentropy",  # 二分类损失函数
    metrics=["accuracy"],
)  # 评估指标

# 训练模型
history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,  # 使用20%的训练数据作为验证集
    epochs=50,  # 训练50个周期
    batch_size=32,  # 每批32个样本
    verbose=1,
)  # 显示训练过程

# 在测试集上评估模型
y_pred = model.predict(X_test).round().astype(int)  # 预测并四舍五入为整数

# 打印测试集准确率和分类报告
print("Accuracy on Test Data:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 绘制混淆矩阵
cm = confusion_matrix(y_test, y_pred)  # 计算混淆矩阵
plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Unstable", "Stable"],
    yticklabels=["Unstable", "Stable"],
)
plt.title("Confusion Matrix")  # 设置标题
plt.xlabel("Predicted")  # 设置x轴标签
plt.ylabel("True")  # 设置y轴标签
plt.show()  # 显示图形

# 绘制训练过程中的准确率和损失
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history["accuracy"], label="Train Accuracy")  # 绘制训练准确率
plt.plot(history.history["val_accuracy"], label="Validation Accuracy")  # 绘制验证准确率
plt.title("Accuracy over Epochs")  # 设置标题
plt.xlabel("Epochs")  # 设置x轴标签
plt.ylabel("Accuracy")  # 设置y轴标签
plt.legend()  # 显示图例

plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Train Loss")  # 绘制训练损失
plt.plot(history.history["val_loss"], label="Validation Loss")  # 绘制验证损失
plt.title("Loss over Epochs")  # 设置标题
plt.xlabel("Epochs")  # 设置x轴标签
plt.ylabel("Loss")  # 设置y轴标签
plt.legend()  # 显示图例

plt.show()  # 显示图形

end_time = datetime.now()  # 记录结束时间
print("\nStart time", start_time)  # 打印开始时间
print("End time", end_time)  # 打印结束时间
print("Time elapsed", end_time - start_time)  # 打印耗时

# 保存模型
model.save("Stability_model.h5")  # 保存模型为.h5文件
print("Model saved to 'Stability_model.h5'")  # 打印保存成功信息

# 故障检测
"""
输入 - [Ia, Ib, Ic, Va, Vb, Vc]
输出 - 0（无故障）或1（故障存在）
"""

# 读取故障检测数据
FaultorNot_data = pd.read_csv(
    r"/kaggle/input/electrical-fault-detection-and-classification/detect_dataset.csv"
)
FaultorNot_data.dropna(axis=1, inplace=True)  # 删除缺失值列
print(FaultorNot_data.head())  # 显示前几行
print(FaultorNot_data.tail())  # 显示后几行
print(FaultorNot_data.isna().sum())  # 检查缺失值

# 特征相关性探索
correlation_matrix = FaultorNot_data.corr()  # 计算相关性矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)  # 绘制热图
plt.title("Correlation Map")  # 设置标题
plt.show()  # 显示图形

# 划分数据集
X = FaultorNot_data.drop("Output (S)", axis=1)  # 特征
y = FaultorNot_data["Output (S)"]  # 标签

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 标准化特征
scaler = StandardScaler()  # 创建标准化对象
X_train = scaler.fit_transform(X_train)  # 拟合并转换训练数据
X_test = scaler.transform(X_test)  # 仅转换测试数据

# 构建ANN模型
model = Sequential(
    [  # 创建顺序模型
        Dense(64, activation="relu", input_dim=X_train.shape[1]),  # 输入层
        Dropout(0.3),  # Dropout层用于正则化
        Dense(32, activation="relu"),  # 隐藏层
        Dropout(0.3),  # Dropout层用于正则化
        Dense(1, activation="sigmoid"),  # 输出层，二分类
    ]
)

model.summary()  # 打印模型摘要

# 编译模型
model.compile(
    optimizer=Adam(learning_rate=0.001),  # 使用Adam优化器
    loss="binary_crossentropy",  # 二分类损失函数
    metrics=["accuracy"],
)  # 评估指标

# 训练模型
history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,  # 使用20%的训练数据作为验证集
    epochs=20,  # 训练20个周期
    batch_size=32,  # 每批32个样本
    verbose=1,
)  # 显示训练过程

# 在测试集上评估模型
y_pred = model.predict(X_test).round().astype(int)  # 预测并四舍五入为整数

# 打印测试集准确率和分类报告
print("Accuracy on Test Data:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# 绘制混淆矩阵
cm = confusion_matrix(y_test, y_pred)  # 计算混淆矩阵
plt.figure(figsize=(6, 5))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Fault", "No fault"],
    yticklabels=["Fault", "No fault"],
)
plt.title("Confusion Matrix")  # 设置标题
plt.xlabel("Predicted")  # 设置x轴标签
plt.ylabel("Real")  # 设置y轴标签
plt.show()  # 显示图形

# 绘制训练过程中的准确率和损失
plt.figure(figsize=(12, 5))

# 准确率图
plt.subplot(1, 2, 1)
plt.plot(
    history.history["accuracy"], label="Train Accuracy", color="blue"
)  # 绘制训练准确率
plt.plot(
    history.history["val_accuracy"], label="Validation Accuracy", color="orange"
)  # 绘制验证准确率
plt.title("Accuracy over Epochs")  # 设置标题
plt.xlabel("Epochs")  # 设置x轴标签
plt.ylabel("Accuracy")  # 设置y轴标签
plt.legend()  # 显示图例

# 损失图
plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Train Loss", color="blue")  # 绘制训练损失
plt.plot(
    history.history["val_loss"], label="Validation Loss", color="orange"
)  # 绘制验证损失
plt.title("Loss over Epochs")  # 设置标题
plt.xlabel("Epochs")  # 设置x轴标签
plt.ylabel("Loss")  # 设置y轴标签
plt.legend()  # 显示图例

plt.show()  # 显示图形

# 保存模型
model.save("fault_detection_model.h5")  # 保存模型为.h5文件
print("Model saved to 'fault_detection_model.h5'")  # 打印保存成功信息

# 故障分类
"""
输入 - [Ia, Ib, Ic, Va, Vb, Vc]
输出 - [G, C, B, A]
示例：
[0, 0, 0, 0] - 无故障
[1, 0, 0, 1] - LG故障（相A与接地之间）
[0, 0, 1, 1] - LL故障（相A与相B之间）
[1, 0, 1, 1] - LLG故障（相A、B与接地之间）
[0, 1, 1, 1] - LLL故障（所有三个相之间）
[1, 1, 1, 1] - LLLG故障（三相对称故障）
"""

# 读取故障分类数据
Faulttype_data = pd.read_csv(
    r"/kaggle/input/electrical-fault-detection-and-classification/classData.csv"
)
print(Faulttype_data.head())  # 显示前几行
print(Faulttype_data.tail())  # 显示后几行
print(Faulttype_data.isna().sum())  # 检查缺失值


# 故障映射
# 映射函数
def map_fault(row):
    # 无故障
    if row["G"] == 0 and row["C"] == 0 and row["B"] == 0 and row["A"] == 0:
        return 0

    # LG故障
    elif row["G"] == 1 and row["C"] == 0 and row["B"] == 0 and row["A"] == 1:
        return 1
    elif row["G"] == 1 and row["C"] == 1 and row["B"] == 0 and row["A"] == 0:
        return 1
    elif row["G"] == 1 and row["C"] == 0 and row["B"] == 1 and row["A"] == 0:
        return 1

    # LL故障
    elif row["G"] == 0 and row["C"] == 0 and row["B"] == 1 and row["A"] == 1:
        return 2
    elif row["G"] == 0 and row["C"] == 1 and row["B"] == 0 and row["A"] == 1:
        return 2
    elif row["G"] == 0 and row["C"] == 1 and row["B"] == 1 and row["A"] == 0:
        return 2

    # LLG故障
    elif row["G"] == 1 and row["C"] == 0 and row["B"] == 1 and row["A"] == 1:
        return 3
    elif row["G"] == 1 and row["C"] == 1 and row["B"] == 0 and row["A"] == 1:
        return 3
    elif row["G"] == 1 and row["C"] == 1 and row["B"] == 1 and row["A"] == 0:
        return 3

    # LLL故障
    elif row["G"] == 0 and row["C"] == 1 and row["B"] == 1 and row["A"] == 1:
        return 4

    # LLLG故障
    elif row["G"] == 1 and row["C"] == 1 and row["B"] == 1 and row["A"] == 1:
        return 5


# 应用映射
Faulttype_data["Fault Type"] = Faulttype_data.apply(map_fault, axis=1)  # 应用映射函数
Faulttype_data.drop(["G", "C", "B", "A"], axis=1, inplace=True)  # 删除不需要的列

# 相关性热图
correlation_matrix = Faulttype_data.corr()  # 计算相关性矩阵
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)  # 绘制热图
plt.title("Correlation Map")  # 设置标题
plt.show()  # 显示图形

# 划分数据
X = Faulttype_data.drop("Fault Type", axis=1)  # 特征
y = Faulttype_data["Fault Type"]  # 标签

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 标准化特征
scaler = StandardScaler()  # 创建标准化对象
X_train = scaler.fit_transform(X_train)  # 拟合并转换训练数据
X_test = scaler.transform(X_test)  # 仅转换测试数据

# 构建ANN模型进行多分类
model = Sequential(
    [  # 创建顺序模型
        Dense(128, activation="relu", input_dim=X_train.shape[1]),  # 输入层
        Dropout(0.3),  # Dropout层用于正则化
        Dense(64, activation="relu"),  # 隐藏层
        Dropout(0.3),  # Dropout层用于正则化
        Dense(6, activation="softmax"),  # 输出层，6个类别
    ]
)

model.summary()  # 打印模型摘要

# 编译模型
model.compile(
    optimizer=Adam(learning_rate=0.001),  # 使用Adam优化器
    loss="sparse_categorical_crossentropy",  # 对于整数标签的损失函数
    metrics=["accuracy"],
)  # 评估指标

# 训练模型
history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,  # 使用20%的训练数据作为验证集
    epochs=50,  # 训练50个周期
    batch_size=32,  # 每批32个样本
    verbose=1,
)  # 显示训练过程

# 在测试集上评估模型
y_pred = model.predict(X_test)  # 进行预测
y_pred_classes = y_pred.argmax(axis=1)  # 获取概率最高的类别

# 打印准确率和分类报告
print("Accuracy on Test Data:", accuracy_score(y_test, y_pred_classes))
print("\nClassification Report:\n", classification_report(y_test, y_pred_classes))

# 绘制混淆矩阵
cm = confusion_matrix(y_test, y_pred_classes)  # 计算混淆矩阵
plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=[
        "No Fault",
        "LG Fault",
        "LL Fault",
        "LLG Fault",
        "LLL Fault",
        "LLLG Fault",
    ],
    yticklabels=[
        "No Fault",
        "LG Fault",
        "LL Fault",
        "LLG Fault",
        "LLL Fault",
        "LLLG Fault",
    ],
)
plt.title("Confusion Matrix")  # 设置标题
plt.xlabel("Predicted")  # 设置x轴标签
plt.ylabel("Real")  # 设置y轴标签
plt.show()  # 显示图形

# 准确率和损失随训练周期变化
plt.figure(figsize=(12, 5))

# 准确率图
plt.subplot(1, 2, 1)
plt.plot(
    history.history["accuracy"], label="Train Accuracy", color="blue"
)  # 绘制训练准确率
plt.plot(
    history.history["val_accuracy"], label="Validation Accuracy", color="orange"
)  # 绘制验证准确率
plt.title("Accuracy over Epochs")  # 设置标题
plt.xlabel("Epochs")  # 设置x轴标签
plt.ylabel("Accuracy")  # 设置y轴标签
plt.legend()  # 显示图例

# 损失图
plt.subplot(1, 2, 2)
plt.plot(history.history["loss"], label="Train Loss", color="blue")  # 绘制训练损失
plt.plot(
    history.history["val_loss"], label="Validation Loss", color="orange"
)  # 绘制验证损失
plt.title("Loss over Epochs")  # 设置标题
plt.xlabel("Epochs")  # 设置x轴标签
plt.ylabel("Loss")  # 设置y轴标签
plt.legend()  # 显示图例

plt.show()  # 显示图形

# 保存模型
model.save("fault_classification_model.h5")  # 保存模型为.h5文件
print("Model saved to 'fault_classification_model.h5'")  # 打印保存成功信息

# 故障检测
# 加载模型
fault_detection_model = load_model("fault_detection_model.h5")  # 加载故障检测模型
print("Model loaded successfully!")

# 智能电表数据模拟
Ia = -134.4076999
Ib = -688.1012042
Ic = 824.5918837
Va = -0.040103509
Vb = 0.008221394
Vc = 0.031882115

smart_meter_data = np.array([[Ia, Ib, Ic, Va, Vb, Vc]])  # 创建输入数据

# 应用标准化（如果在训练时使用了StandardScaler）
new_data_scaled = scaler.transform(smart_meter_data)  # 使用与训练相同的标准化器

# 使用模型进行预测
predicted_probabilities = fault_detection_model.predict(new_data_scaled)  # 进行预测
predicted_class = np.round(predicted_probabilities)  # 获取预测类别
predicted_class = predicted_class.item()  # 转换为标量

# 故障映射
if predicted_class == 1:
    predicted_fault = "Fault"  # 故障
elif predicted_class == 0:
    predicted_fault = "No Fault"  # 无故障
print(f"Predicted Fault Type: {predicted_fault}")  # 打印预测结果

# 加载故障分类模型
fault_classification_model = load_model(
    "fault_classification_model.h5"
)  # 加载故障分类模型
print("Model loaded successfully!")

# 故障分类
if predicted_class == 1:  # 如果检测到故障
    smart_meter_data = np.array([[Ia, Ib, Ic, Va, Vb, Vc]])  # 创建输入数据
    new_data_scaled = scaler.transform(smart_meter_data)  # 标准化输入数据
    predicted_probabilities = fault_classification_model.predict(
        new_data_scaled
    )  # 进行预测
    predicted_class = np.argmax(predicted_probabilities, axis=1)  # 获取预测类别索引

    # 故障映射
    fault_types = [
        "No Fault",
        "LG Fault",
        "LL Fault",
        "LLG Fault",
        "LLL Fault",
        "LLLG Fault",
    ]  # 故障类型
    predicted_fault_type = fault_types[predicted_class[0]]  # 获取预测的故障类型

    print(f"Predicted Fault Type: {predicted_fault_type}")  # 打印预测的故障类型
else:
    print("No fault detected")  # 如果未检测到故障
