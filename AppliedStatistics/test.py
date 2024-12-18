from scipy.stats import norm
from scipy.stats import t
import math


def P_I(x):
    return math.e ** (-5.6) * 5.6**x / math.factorial(x)


def z_fu_1(args):
    # 反求 Z 值
    z_value = norm.ppf(args)
    print(f"累计概率为{args}的Z分数", z_value)
    return z_value


def name():
    import numpy as np
    import scipy.stats as stats
    import matplotlib.pyplot as plt
    import seaborn as sns

    # 数据
    data = np.array([112.3, 97.0, 92.7, 99.2, 95.8, 103.5, 86.0, 89.0, 102.0, 86.7])

    # 绘制直方图
    sns.histplot(data, kde=True)
    plt.title("Histogram of Concrete Compressive Strength")
    plt.xlabel("Compressive Strength (MPa)")
    plt.ylabel("Frequency")
    plt.show()

    # Q-Q图
    stats.probplot(data, dist="norm", plot=plt)
    plt.title("Q-Q Plot")
    plt.show()

    # Shapiro-Wilk检验
    stat, p_value = stats.shapiro(data)
    print(f"Shapiro-Wilk检验统计量: {stat}, p值: {p_value}")

    # # 计算样本均值和标准差
    # mean_strength = np.mean(data)
    # std_strength = np.std(data, ddof=1)  # 样本标准差
    # n = len(data)

    # # 计算t值
    # t_value = (mean_strength - 100) / (std_strength / np.sqrt(n))

    # # 计算p值（单尾检验）
    # p_value_ttest = stats.t.cdf(t_value, df=n - 1)

    # print(f"样本均值: {mean_strength:.2f}, 样本标准差: {std_strength:.2f}")
    # print(f"t值: {t_value:.4f}, p值: {p_value_ttest:.4f}")


import numpy as np

mean = 0
for i in [112.3, 97.0, 92.7, 99.2, 95.8, 103.5, 86.0, 89.0, 102.0, 86.7]:
    mean += i / 10
print(mean)
S = 0
for i in [112.3, 97.0, 92.7, 99.2, 95.8, 103.5, 86.0, 89.0, 102.0, 86.7]:
    S += (i - mean) ** 2 / 9
S = math.sqrt(S)
print(S)

# 生成一个从0.1到1的数组，步长为0.1
arr = np.arange(0.1, 1.1, 0.1)
for i in arr:
    print(z_fu_1(i) * S + mean)

# print(P_I(0) + P_I(1) + P_I(2))
# print(P_I(3))
# name()
print(sorted([112.3, 97.0, 92.7, 99.2, 95.8, 103.5, 86.0, 89.0, 102.0, 86.7]))
