import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 数据
data = [
    418,
    434,
    454,
    421,
    437,
    463,
    421,
    439,
    465,
    422,
    446,
    425,
    447,
    427,
    448,
    431,
    453,
]

# 计算四分位数
sorted_data = np.sort(data)
Q1 = np.percentile(sorted_data, 25)  # 第一四分位数
Q3 = np.percentile(sorted_data, 75)  # 第三四分位数
IQR = Q3 - Q1  # 四分位距

# 打印结果
print("排序后的数组:", sorted_data)
print("第一四分位数 (Q1):", Q1)
print("第三四分位数 (Q3):", Q3)
print("四分位距 (IQR):", IQR)

# 创建箱线图
plt.figure(figsize=(10, 6))
sns.boxplot(data=data, color="lightgray")  # 设置颜色为灰色

# 添加数据点
for i, value in enumerate(data):
    plt.text(0, value, str(value), ha="center", va="bottom")

# 添加标题和标签
plt.title("Box Plot of Given Data")
plt.ylabel("Values")
plt.xticks([0], ["Data"])
plt.grid(axis="y")

# 显示图形
plt.show()
