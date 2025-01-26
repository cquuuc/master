import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

# 设置参数
alpha = 0.05  # 例如，显著性水平
n = 3  # 自由度 n-1
m = 2  # 自由度 m-1

# 计算 F 分布的临界值 F_{a/2, n-1, m-1}
# 这里的 alpha/2 是因为我们通常需要计算双尾的临界值
f_critical_value = stats.f.ppf(alpha / 2, n - 1, m - 1)

print(f"F_{alpha/2}, {n-1}, {m-1} 的临界值为: {f_critical_value}")


# 计算 T_{alpha/2, n-1} 值
t_alpha_over_2 = t.ppf(alpha / 2, 30 - 1)
