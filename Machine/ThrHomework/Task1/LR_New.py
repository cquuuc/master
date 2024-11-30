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
feature_counts = [1, 2, 3]

# # 绘制原始数据集
# plt.scatter(X, y, color="blue", label="Original Data")

# 设置子图的行数和列数
rows = 2
cols = 3

# 创建一个新的图形，并设置子图布局
fig, axes = plt.subplots(rows, cols, figsize=(15, 10))

# 对每个特征数量进行建模和绘图
for i, count in enumerate(feature_counts):
    # 计算当前子图的行索引和列索引
    row = i // cols
    col = i % cols

    # 在当前子图中绘制原始数据集
    axes[row, col].scatter(X, y, color="blue", label="Original Data")

    # 创建多项式特征
    poly_reg = PolynomialFeatures(count)
    X_poly = poly_reg.fit_transform(X)

    # 使用 L1 正则化的线性回归建模
    lasso_model = make_pipeline(poly_reg, Lasso(alpha=0.1))
    lasso_model.fit(X_poly, y)
    y_pred_lasso = lasso_model.predict(X_poly)
    # lasso_model.predict(poly_reg.fit_transform(X_poly))

    # 使用 L2 正则化的线性回归建模
    ridge_model = make_pipeline(poly_reg, Ridge(alpha=0.1))
    ridge_model.fit(X_poly, y)
    y_pred_ridge = ridge_model.predict(X_poly)
    # print("My1", ridge_model.score(X_poly, y))
    # print(ridge_model.coef_, ridge_model.intercept_)
    print(
        lasso_model.named_steps["lasso"].coef_,
        lasso_model.named_steps["lasso"].intercept_,
    )
    print(
        ridge_model.named_steps["ridge"].coef_,
        ridge_model.named_steps["ridge"].intercept_,
    )

    # 在当前子图中绘制拟合曲线
    # axes[row, col].plot(X, y_pred_lasso, label=f"Lasso (Degree {count})")
    # axes[row, col].plot(X, y_pred_ridge, label=f"Ridge (Degree {count})")
    axes[row, col].plot(
        X,
        y_pred_lasso,
        label=f"lasso_model score:{lasso_model.score(X_poly, y)}",
    )
    axes[row, col].plot(
        X,
        y_pred_ridge,
        label=f"ridge_model score:{ridge_model.score(X_poly, y)}",
    )

    # 设置子图的标题和标签
    axes[row, col].set_title(f"Degree {count}")
    axes[row, col].set_xlabel("X")
    axes[row, col].set_ylabel("y")
    axes[row, col].legend()

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.show()
