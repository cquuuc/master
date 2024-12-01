import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 定义函数 f(x, y)
def f(x, y):
    return 3 * x**2 + 5 * y**2 + 6 * x * y + 7 * x + 1


# 定义偏导数
def df(x, y):
    df_dx = 6 * x + 6 * y + 7
    df_dy = 10 * y + 6 * x
    return np.array([df_dx, df_dy])


# 定义点
x0, y0 = 0, 0
x1, y1 = -1.4, 0

# 计算梯度
gradient_0 = df(x0, y0)
gradient_1 = df(x1, y1)

# 创建网格以绘制三维图
x_values = np.linspace(-3, 3, 100)
y_values = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = f(X, Y)

# 创建三维图形
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection="3d")

# 绘制表面
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)

# 绘制边界
ax.contour3D(X, Y, Z, levels=30, cmap="viridis", linewidths=0.5)

# 标记点 (x0, y0) 和 (x1, y1)
ax.scatter(x0, y0, f(x0, y0), color="red", s=100, label="(0, 0)")
ax.scatter(x1, y1, f(x1, y1), color="blue", s=100, label="(-1.4, 0)")

# 绘制梯度向量
ax.quiver(
    x0,
    y0,
    f(x0, y0),
    gradient_0[0],
    gradient_0[1],
    0,
    color="orange",
    length=0.5,
    label="Gradient at (0, 0)",
)
ax.quiver(
    x1,
    y1,
    f(x1, y1),
    gradient_1[0],
    gradient_1[1],
    0,
    color="green",
    length=0.5,
    label="Gradient at (-1.4, 0)",
)

# 设置图形属性
ax.set_title("3D Surface plot of f(x, y) = 3x^2 + 5y^2 + 6xy + 7x + 1")
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("f(x, y)")

# 添加图例
ax.legend()

# 显示图形
plt.show()
