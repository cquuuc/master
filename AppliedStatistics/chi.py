from scipy.stats import chi2


# 自由度
df = 2

# 置信水平
alpha = 0.05

# 计算卡方分布的临界值

chi_squared_value2 = chi2.ppf(1 - alpha, df)

print(f"χ²_{alpha}, {df} = {chi_squared_value2:.4f}")
