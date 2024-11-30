import numpy as np


def calculate_theta_lambda(x, max_iterations=1000, tolerance=1e-6):
    n = len(x)
    x_bar = np.mean(x)

    # 初始化 theta
    theta = x_bar  # 可以选择初始值为均值
    lambda_value = 0  # 初始 lambda 值

    for _ in range(max_iterations):
        # 计算新的 lambda
        denominator = 1 / n * np.sum(x**2) - theta**2 - 2 * theta

        # 检查分母是否为零或接近零
        if abs(denominator) < 1e-10:
            raise ValueError(
                "Denominator for lambda calculation is too close to zero. Please check your data."
            )

        lambda_value = 2 / denominator

        # 计算新的 theta
        new_theta = x_bar - 1 / lambda_value

        # 限制 theta 的范围
        new_theta = np.clip(new_theta, -1e10, 1e10)  # 限制 theta 的范围

        # 检查收敛
        if abs(new_theta - theta) < tolerance:
            break

        theta = new_theta

    return theta, lambda_value


# 示例数据
data = np.array([3.11, 0.64, 2.55, 2.20, 5.44, 3.42, 10.39, 8.93, 17.82, 1.30])
theta, lambda_value = calculate_theta_lambda(data)

print(f"theta: {theta}, lambda: {lambda_value}")
