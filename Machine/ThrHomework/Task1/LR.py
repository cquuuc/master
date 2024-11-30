import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

# 生成人工数据集
np.random.seed(0)
X = np.random.rand(100, 1) * 10
y = 2 * X + np.random.randn(100, 1)

# 设置不同的特征数量
feature_counts = [1, 2, 3, 4, 5]

# 绘制原始数据集
plt.scatter(X, y, color="blue", label="Original Data")

# 对每个特征数量进行建模和绘图
for count in feature_counts:
    # 创建多项式特征
    polynomial_features = PolynomialFeatures(degree=count)
    X_poly = polynomial_features.fit_transform(X)

    # 使用 L1 正则化的线性回归建模
    lasso_model = make_pipeline(polynomial_features, Lasso(alpha=0.1))
    lasso_model.fit(X_poly, y)
    y_pred_lasso = lasso_model.predict(X_poly)

    # 使用 L2 正则化的线性回归建模
    ridge_model = make_pipeline(polynomial_features, Ridge(alpha=0.1))
    ridge_model.fit(X_poly, y)
    y_pred_ridge = ridge_model.predict(X_poly)
    print(
        lasso_model.named_steps["lasso"].coef_,
        lasso_model.named_steps["lasso"].intercept_,
    )
    print(
        ridge_model.named_steps["ridge"].coef_,
        ridge_model.named_steps["ridge"].intercept_,
    )

    # 绘制拟合曲线
    plt.plot(X, y_pred_lasso, label=f"Lasso (Degree {count})")
    plt.plot(X, y_pred_ridge, label=f"Ridge (Degree {count})")

    # 设置图例和标题
    plt.legend()
    plt.title("L1 and L2 Regularization in Linear Regression")
    plt.xlabel("X")
    plt.ylabel("y")

    # 显示图形
    plt.show()
