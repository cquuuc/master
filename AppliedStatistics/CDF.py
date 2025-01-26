from scipy.stats import norm
from scipy.stats import t

# 已知的 CDF 值
cdf_value = norm.cdf(-2.67)  # 计算的 CDF 值
print("CDF Value:", cdf_value, 1 - cdf_value)


# 反求 Z 值
c_c_c_x = 0.1
z_value = norm.ppf(c_c_c_x)
print(f"累计概率为{c_c_c_x}的Z分数", z_value)


# 计算 Z_{a/2} 值
alpha = 0.05
z_a_over_2 = norm.ppf(1 - alpha / 2)
print(f"Z_a/2 value for {1- alpha} confidence level:", z_a_over_2)


# 输入参数
n = 52  # 样本量
alpha = 0.05  # 显著性水平（例如 0.05 对应于 95% 置信水平）
S = 2.5  # 样本标准差

# 计算自由度
df = n

# 计算 T_{alpha/2, n-1} 值
t_alpha_over_2 = t.ppf(1 - alpha / 2, df)

# 计算置信区间的宽度
margin_of_error = t_alpha_over_2 * (S / (n**0.5))
confidence_interval_width = 2 * margin_of_error
# 输出结果
print(f"T_{{alpha/2, {df}}} value:", t_alpha_over_2)
print(f"置信区间的宽度:", confidence_interval_width)


# 自由度
df = 9
# t值
t_value = 0.1615
# 计算P(T <= ？)
p_value = t.cdf(t_value, df)
# 计算P(T >= ？)
print(f"计算P(T >= {t_value}):{1 - p_value:.3f}")
# 显著性水平
alpha = 0.01
# 计算上尾临界值
t_critical = t.ppf(alpha, df)
print(f"T({alpha}, {df} ) 的临界值为: {t_critical:.3f}")


print(t.ppf(1 - 0.05, 7))
