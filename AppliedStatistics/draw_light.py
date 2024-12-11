import matplotlib.pyplot as plt
import numpy as np

# 固定a的值
a = 1.0  # 可以根据需要调整

# 定义两个离散的theta值
theta_values = [np.pi / 4, -np.pi / 3]  # 45度和60度

# 生成x坐标的值
x = np.linspace(-2, 3, 100)

# 创建绘图
fig, ax = plt.subplots(figsize=(8, 6))

# 设置x轴和y轴的范围
ax.set_xlim(-2, 3)
ax.set_ylim(-2, 2)

# 画x轴和y轴
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)

# 绘制固定的垂直线x=a
ax.axvline(x=a, color="green", linestyle="--", label=f"x = {a}")

# 绘制y=1的水平线
ax.axhline(y=1, color="orange", linestyle="--", label="y = 1")

# 绘制每个theta对应的直线和交点
for theta in theta_values:
    # 计算直线的斜率
    slope = np.tan(theta)

    # 计算直线的y坐标
    y = slope * (x - a) + 1  # 通过点M(a, 1)的直线方程

    # 计算交点X的坐标
    X_x = a + np.tan(theta)
    print(a, np.tan(theta))

    # 绘制直线
    ax.plot(x, y, label=f"θ = {theta * 180 / np.pi:.1f}°")

    # 绘制交点
    # ax.plot(X_x, 0, "ro")  # 交点X
    # ax.text(X_x, 0.1, f"X({X_x:.2f}, 0)", fontsize=10, ha="center")

# 绘制点M(a, 1)
ax.plot(a, 1, "bo", markersize=6, label=f"M({a}, 1)")
ax.text(a, 1.1, f"M({a}, 1)", fontsize=10, ha="center")

# 添加图例和标题
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("Lines through point M and intersection points X")
ax.legend()

# 显示图形
plt.grid()
plt.show()
