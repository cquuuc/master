from scipy.stats import norm
from scipy.stats import t

# 已知的 CDF 值
cdf_value = norm.cdf(0.1754)  # 计算的 CDF 值
print("CDF Value:", cdf_value)


# 反求 Z 值
z_value = norm.ppf(0.1754)
print("Z Value:", z_value)


# 计算 Z_{a/2} 值
alpha = 0.01
z_a_over_2 = norm.ppf(1 - alpha / 2)
print(f"Z_a/2 value for {1- alpha} confidence level:", z_a_over_2)


# 输入参数
n = 17  # 样本量
alpha = 0.05  # 显著性水平（例如 0.05 对应于 95% 置信水平）
S = 175  # 样本标准差

# 计算自由度
df = n - 1

# 计算 T_{alpha/2, n-1} 值
t_alpha_over_2 = t.ppf(1 - alpha / 2, df)

# 计算置信区间的宽度
margin_of_error = t_alpha_over_2 * (S / (n**0.5))
confidence_interval_width = 2 * margin_of_error
# 输出结果
print(f"T_{{alpha/2, {df}}} value:", t_alpha_over_2)
print(f"置信区间的宽度:", confidence_interval_width)
