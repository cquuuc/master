import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

# 生成人工数据集
np.random.seed(0)
X = np.random.rand(100, 1) * 10
y = 2 * X.squeeze() + np.random.randn(100) * 2

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 创建 Ridge 模型并训练
ridge_model = Ridge(alpha=0.5)  # alpha 是正则化强度
ridge_model.fit(X_train, y_train)

# 预测
y_pred = ridge_model.predict(X_test)

# 打印 Ridge 模型的系数
print("Ridge Coefficients:", ridge_model.coef_)

# 绘制结果
plt.scatter(X_test, y_test, color="blue", label="True Values")
plt.scatter(X_test, y_pred, color="red", label="Predictions")
plt.title("Ridge Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
