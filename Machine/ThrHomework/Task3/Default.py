# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.animation import FuncAnimation


# # 定义 Rosenbrock 函数
# def rosenbrock(x, y, a=1, b=100):
#     return (a - x) ** 2 + b * (y - x**2) ** 2


# # 定义 Rosenbrock 函数的偏导数
# def d_rosenbrock(x, y, a=1, b=100):
#     df_dx = -2 * (a - x) - 4 * b * x * (y - x**2)
#     df_dy = 2 * b * (y - x**2)
#     return np.array([df_dx, df_dy])


# # 初始化参数
# learning_rate = 0.001
# iterations = 100

# # 初始化点
# x = -0.5  # 从一个远离最小值的点开始
# y = 3

# # 创建网格以绘制三维图
# x_values = np.linspace(-2, 2, 100)
# y_values = np.linspace(-1, 3, 100)
# X, Y = np.meshgrid(x_values, y_values)
# Z = rosenbrock(X, Y)

# # 创建三维图形
# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(111, projection="3d")

# # 绘制表面
# ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)

# # 初始化点的散点图
# (point,) = ax.plot([], [], [], "ro", markersize=10)


# # 更新函数
# def update(frame):
#     global x, y
#     # 计算损失和梯度
#     loss = rosenbrock(x, y)
#     gradient = d_rosenbrock(x, y)

#     # 输出当前损失和梯度
#     # print(f"Iteration {frame + 1}: Loss = {loss:.4f}, Gradient = {gradient}")
#     ax.set_title(f"Iteration {frame + 1}: Loss = {loss:.4f}, Gradient = {gradient}")

#     # 更新点的位置（普通梯度下降）
#     x -= learning_rate * gradient[0]
#     y -= learning_rate * gradient[1]

#     # 更新散点图的位置
#     point.set_data([x], [y])  # 需要将 x 和 y 包裹在列表中
#     point.set_3d_properties(rosenbrock(x, y))

#     return (point,)


# # 设置图形属性
# # ax.set_title('Gradient Descent on Rosenbrock Function')
# ax.set_xlabel("X axis")
# ax.set_ylabel("Y axis")
# ax.set_zlabel("f(x, y)")

# # 创建动画
# ani = FuncAnimation(fig, update, frames=iterations, blit=False, repeat=False)

# # 显示图形
# plt.show()


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation


# 定义 Rosenbrock 函数
def rosenbrock(x, y, a=1, b=100):
    return (a - x) ** 2 + b * (y - x**2) ** 2


# 定义 Rosenbrock 函数的偏导数
def d_rosenbrock(x, y, a=1, b=100):
    df_dx = -2 * (a - x) - 4 * b * x * (y - x**2)
    df_dy = 2 * b * (y - x**2)
    return np.array([df_dx, df_dy])


# 初始化参数
learning_rate = 0.001
iterations = 100

# 初始化点
x = -0.5  # 从一个远离最小值的点开始
y = 3

# 创建网格以绘制三维图
x_values = np.linspace(-2, 2, 100)
y_values = np.linspace(-1, 3, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = rosenbrock(X, Y)

# 创建三维图形
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(211, projection="3d")

# 绘制表面
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)

# 初始化点的散点图
(point,) = ax.plot([], [], [], "ro", markersize=10)

# 记录损失值
mse_values = []  # 用于记录每次迭代的损失值


# 更新函数
def update(frame):
    global x, y
    # 计算损失和梯度
    loss = rosenbrock(x, y)
    gradient = d_rosenbrock(x, y)

    # 输出当前损失和梯度
    ax.set_title(f"Iteration {frame + 1}: Loss = {loss:.4f}, Gradient = {gradient}")

    # 更新点的位置（普通梯度下降）
    x -= learning_rate * gradient[0]
    y -= learning_rate * gradient[1]

    # 记录当前损失
    mse_values.append(loss)

    # 更新散点图的位置
    point.set_data([x], [y])  # 需要将 x 和 y 包裹在列表中
    point.set_3d_properties(rosenbrock(x, y))

    # 更新 MSE 曲线
    mse_line.set_data(range(len(mse_values)), mse_values)
    if mse_values:  # 确保 mse_values 不为空
        ax_mse.set_ylim(0, np.max(mse_values) + 10)  # 动态调整 y 轴范围

    return (
        point,
        mse_line,
    )


# 设置图形属性
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("f(x, y)")

# 创建 MSE 曲线的子图
ax_mse = fig.add_subplot(212)
ax_mse.set_xlim(0, iterations)
ax_mse.set_ylim(0, 10)  # 初始 y 轴范围
ax_mse.set_xlabel("Iterations")
ax_mse.set_ylabel("MSE")
(mse_line,) = ax_mse.plot([], [], color="blue", label="MSE")
ax_mse.legend()

# 创建动画
ani = FuncAnimation(fig, update, frames=iterations, blit=False, repeat=False)

# 显示图形
plt.show()
