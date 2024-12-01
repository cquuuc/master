import numpy as np
import matplotlib.pyplot as plt


# 定义函数和导数
def f(x):
    return x**2 - 3 * x + 2


def f_prime(x):
    return 2 * x - 3


# 定义 x 的范围
x_values = np.linspace(-1, 4, 100)
y_values = f(x_values)

# 定义给定的点
x0 = 0
x1 = 0.6
y0 = f(x0)
y1 = f(x1)

# 计算导数（动量）
slope0 = f_prime(x0)
slope1 = f_prime(x1)

# 创建图形
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label="f(x) = x^2 - 3x + 2", color="blue")
plt.scatter([x0, x1], [y0, y1], color="red")  # 标记点
plt.text(x0, y0, f"({x0}, {y0})", fontsize=10, verticalalignment="bottom")
plt.text(x1, y1, f"({x1}, {y1})", fontsize=10, verticalalignment="bottom")

# 绘制切线
plt.plot(
    [x0, x0 + 1],
    [y0, y0 + slope0],
    color="green",
    linestyle="--",
    label="Tangent at x0",
)
plt.plot(
    [x1, x1 + 1],
    [y1, y1 + slope1],
    color="orange",
    linestyle="--",
    label="Tangent at x1",
)

# 设置图形属性
plt.title("Function and Tangents")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color="black", linewidth=0.5, ls="--")
plt.axvline(0, color="black", linewidth=0.5, ls="--")
plt.grid()
plt.legend()
plt.xlim(-1, 4)
plt.ylim(-1, 3)

# 显示图形
plt.show()
