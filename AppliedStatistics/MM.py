import numpy as np


def calculate_theta_lambda(x, max_iterations=1000, tolerance=1e-6):
    n = len(x)
    x_bar = np.mean(x)

    # 初始化 theta 和 lambda
    theta = x_bar  # 初始值为均值
    lambda_value = 1.0  # 初始 lambda 值，避免除以零

    for _ in range(max_iterations):
        # 计算新的 lambda
        denominator = 1 / n * np.sum(x**2) - theta**2 - 2 * theta

        # 检查分母是否为零或接近零
        if abs(denominator) < 1e-10:
            print("Denominator too close to zero, stopping iteration.")
            break

        lambda_value = 2 / denominator

        # 检查 lambda 是否为零或无穷大
        if np.isinf(lambda_value) or lambda_value == 0:
            print("Lambda is zero or infinite, stopping iteration.")
            break

        # 计算新的 theta
        new_theta = x_bar - 1 / lambda_value

        # 检查 theta 是否为无穷大
        if np.isinf(new_theta):
            print("Theta is infinite, stopping iteration.")
            break

        # 检查收敛
        if abs(new_theta - theta) < tolerance:
            theta = new_theta
            break

        theta = new_theta

    return theta, lambda_value


# 示例数据
data = np.array([3.11, 0.64, 2.55, 2.20, 5.44, 3.42, 10.39, 8.93, 17.82, 1.30])
theta, lambda_value = calculate_theta_lambda(data)

print(f"theta: {theta}, lambda: {lambda_value}")
