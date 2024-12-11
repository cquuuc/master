import numpy as np
from scipy.stats import norm
from scipy.stats import shapiro


def shapiro_wilk_test1(data):
    # Step 1: Sort the data
    n = len(data)
    sorted_data = np.sort(data)

    # Step 2: Calculate the mean and standard deviation
    mean = np.mean(sorted_data)
    std_dev = np.std(sorted_data, ddof=1)

    # Step 3: Calculate the coefficients a_i
    # Calculate the expected values from the standard normal distribution
    m = norm.ppf((np.arange(1, n + 1) - 0.375) / (n + 0.25))

    # Calculate the a_i coefficients
    a = m / np.sqrt(np.sum(m**2))

    # Step 4: Calculate W statistic
    W = (np.sum(a * sorted_data)) ** 2 / np.sum((sorted_data - mean) ** 2)

    return W, a


def shapiro_wilk_test2(data, alpha=0.05):
    # Perform Shapiro-Wilk test using scipy's built-in function
    W, p_value = shapiro(data)

    # Print the W statistic and p-value
    print("Shapiro-Wilk W statistic:", W)
    print("p-value:", p_value)

    # Decision based on p-value
    if p_value < alpha:
        print("拒绝原假设 H0：数据不符合正态分布")
    else:
        print("不能拒绝原假设 H0：数据符合正态分布")


# Example data
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

# Perform Shapiro-Wilk test
W_statistic, a_coefficients = shapiro_wilk_test1(data)
print("Shapiro-Wilk W statistic:", W_statistic)
# print("Coefficients a_i:", a_coefficients)
shapiro_wilk_test2(data)
