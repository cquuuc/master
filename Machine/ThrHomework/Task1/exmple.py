import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge, Lasso

# 生成随机数据
rng = np.random.RandomState(1)
x = 10 * rng.rand(60)
y = x**2 / 10 + 0.9 * rng.randn(60)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(
    x[:, np.newaxis],
    y,
    test_size=0.27,
    random_state=42,
)

# 定义多项式的度数范围
degrees = list(range(2, 13))
# 初始化分数列表
scores_test_ridge = []
scores_train_ridge = []
scores_test_lasso = []
scores_train_lasso = []

# 循环训练模型并计算得分
for i in degrees:
    # Ridge模型
    ridge_model = make_pipeline(PolynomialFeatures(degree=i), Ridge(alpha=0.1))
    ridge_model.fit(X_train, y_train)
    scores_test_ridge.append(ridge_model.score(X_test, y_test))
    scores_train_ridge.append(ridge_model.score(X_train, y_train))

    # Lasso模型
    lasso_model = make_pipeline(PolynomialFeatures(degree=i), Lasso(alpha=0.1))
    lasso_model.fit(X_train, y_train)
    scores_test_lasso.append(lasso_model.score(X_test, y_test))
    scores_train_lasso.append(lasso_model.score(X_train, y_train))

# 创建一个窗口，设置子图
plt.figure(figsize=(12, 6))

# Ridge得分图
plt.subplot(1, 2, 1)
plt.plot(degrees, scores_train_ridge, "r-o", label="Train Ridge")
plt.plot(degrees, scores_test_ridge, "b-o", label="Test Ridge")
plt.xlabel("Polynomial Degree")
plt.ylabel("Score")
plt.title("Ridge Regression Scores")
plt.legend()

# Lasso得分图
plt.subplot(1, 2, 2)
plt.plot(degrees, scores_train_lasso, "g-o", label="Train Lasso")
plt.plot(degrees, scores_test_lasso, "y-o", label="Test Lasso")
plt.xlabel("Polynomial Degree")
plt.ylabel("Score")
plt.title("Lasso Regression Scores")
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()
