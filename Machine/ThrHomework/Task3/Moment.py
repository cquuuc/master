# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.animation import FuncAnimation
# from scipy.optimize import minimize


# # 定义 Rosenbrock 函数
# def rosenbrock(x):
#     a = 1
#     b = 100
#     return (a - x[0]) ** 2 + b * (x[1] - x[0] ** 2) ** 2


# # 定义 Rosenbrock 函数的偏导数
# def d_rosenbrock(x, a=1, b=100):
#     df_dx = -2 * (a - x[0]) - 4 * b * x[0] * (x[1] - x[0] ** 2)
#     df_dy = 2 * b * (x[1] - x[0] ** 2)
#     return np.array([df_dx, df_dy])


# # 初始化参数
# learning_rate = 0.001
# momentum = 0.7
# iterations = 30

# # 初始化点，选择一个远离最小值的点
# x = np.array([-0.5, 3])  # 初始点

# # 初始化动量
# v = np.zeros(2)

# # 创建网格以绘制三维图
# x_values = np.linspace(-2, 2, 100)
# y_values = np.linspace(-1, 3, 100)
# X, Y = np.meshgrid(x_values, y_values)
# Z = rosenbrock([X, Y])

# # 创建三维图形
# fig = plt.figure(figsize=(12, 8))
# ax = fig.add_subplot(111, projection="3d")

# # 绘制表面
# ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)

# # 初始化点的散点图
# (point,) = ax.plot([], [], [], "ro", markersize=10)

# # 记录动量优化的轨迹
# momentum_trajectory = []


# # 更新函数
# def update(frame):
#     global x, v
#     # 计算损失和梯度
#     loss = rosenbrock(x)
#     gradient = d_rosenbrock(x)

#     # 输出当前损失和梯度
#     ax.set_title(f"Iteration {frame + 1}: Loss = {loss:.4f}, Gradient = {gradient}")

#     # 更新动量
#     v = momentum * v - learning_rate * gradient

#     # 更新点的位置
#     x += v

#     # 记录轨迹
#     momentum_trajectory.append(x.copy())

#     # 更新散点图的位置
#     point.set_data([x[0]], [x[1]])  # 需要将 x 和 y 包裹在列表中
#     point.set_3d_properties(rosenbrock(x))

#     return (point,)


# # 设置图形属性
# ax.set_xlabel("X axis")
# ax.set_ylabel("Y axis")
# ax.set_zlabel("f(x, y)")

# # 创建动画
# ani = FuncAnimation(fig, update, frames=iterations, blit=False, repeat=False)

# # 使用内置优化函数进行优化
# result = minimize(rosenbrock, x, method="L-BFGS-B")
# print(f"SciPy Result: {result.x}, Function Value: {rosenbrock(result.x)}")


# # 在动画结束后标记 SciPy 的结果
# def finalize_plot():
#     ax.scatter(
#         result.x[0],
#         result.x[1],
#         rosenbrock(result.x),
#         color="blue",
#         s=100,
#         label="SciPy Result",
#     )
#     ax.legend()
#     plt.show()


# # 在动画结束后调用 finalize_plot
# ani.event_source.stop()
# finalize_plot()
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from scipy.optimize import minimize


# 定义 Rosenbrock 函数
def rosenbrock(x):
    a = 1
    b = 100
    return (a - x[0]) ** 2 + b * (x[1] - x[0] ** 2) ** 2


# 定义 Rosenbrock 函数的偏导数
def d_rosenbrock(x, a=1, b=100):
    df_dx = -2 * (a - x[0]) - 4 * b * x[0] * (x[1] - x[0] ** 2)
    df_dy = 2 * b * (x[1] - x[0] ** 2)
    return np.array([df_dx, df_dy])


# 初始化参数
learning_rate = 0.001
momentum = 0.7
iterations = 30

# 初始化点，选择一个远离最小值的点
x = np.array([-0.5, 3])  # 初始点

# 初始化动量
v = np.zeros(2)

# 创建网格以绘制三维图
x_values = np.linspace(-2, 2, 100)
y_values = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x_values, y_values)
Z = rosenbrock([X, Y])

# 创建三维图形
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(211, projection="3d")

# 绘制表面
ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8)

# 初始化点的散点图
(point,) = ax.plot([], [], [], "ro", markersize=10)

# 记录动量优化的轨迹
momentum_trajectory = []
mse_values = []  # 用于记录每次迭代的损失值

# 创建 MSE 曲线的子图
ax_mse = fig.add_subplot(212)
ax_mse.set_xlim(0, iterations)
ax_mse.set_ylim(0, 750)  # 根据 Rosenbrock 函数的值调整 y 轴范围
ax_mse.set_xlabel("Iterations")
ax_mse.set_ylabel("MSE")
(mse_line,) = ax_mse.plot([], [], color="blue", label="MSE")
ax_mse.legend()


# 更新函数
def update(frame):
    global x, v
    # 计算损失和梯度
    loss = rosenbrock(x)
    gradient = d_rosenbrock(x)

    # 输出当前损失和梯度
    ax.set_title(f"Iteration {frame + 1}: Loss = {loss:.4f}, Gradient = {gradient}")

    # 更新动量
    v = momentum * v - learning_rate * gradient

    # 更新点的位置
    x += v

    # 记录轨迹
    momentum_trajectory.append(x.copy())
    mse_values.append(loss)  # 记录当前损失

    # 更新散点图的位置
    point.set_data([x[0]], [x[1]])  # 需要将 x 和 y 包裹在列表中
    point.set_3d_properties(rosenbrock(x))

    # 更新 MSE 曲线
    mse_line.set_data(range(len(mse_values)), mse_values)

    return (point, mse_line)


# 设置图形属性
ax.set_xlabel("X axis")
ax.set_ylabel("Y axis")
ax.set_zlabel("f(x, y)")

# 创建动画
ani = FuncAnimation(fig, update, frames=iterations, blit=False, repeat=False)

# 使用内置优化函数进行优化
result = minimize(rosenbrock, x, method="L-BFGS-B")
print(f"SciPy Result: {result.x}, Function Value: {rosenbrock(result.x)}")


# 在动画结束后标记 SciPy 的结果
def finalize_plot():
    ax.scatter(
        result.x[0],
        result.x[1],
        rosenbrock(result.x),
        color="blue",
        s=100,
        label="SciPy Result",
    )
    ax.legend()
    plt.show()


# 在动画结束后调用 finalize_plot
ani.event_source.stop()
finalize_plot()
