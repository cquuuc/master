import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt


def kolmogorov_smirnov_test(data, distribution="norm", alpha=0.05):
    # Step 1: Sort the data
    n = len(data)
    sorted_data = np.sort(data)

    # Step 2: Calculate the empirical distribution function (EDF)
    F_n = np.arange(1, n + 1) / n

    # Step 3: Calculate the theoretical distribution function
    if distribution == "norm":
        # Assuming normal distribution with mean and std from data
        mean = np.mean(data)
        std_dev = np.std(data, ddof=1)
        F = stats.norm.cdf(sorted_data, loc=mean, scale=std_dev)
    elif distribution == "expon":
        # Assuming exponential distribution with scale from data
        scale = np.mean(data)
        F = stats.expon.cdf(sorted_data, scale=scale)
    else:
        raise ValueError("Unsupported distribution type")

    # Step 4: Calculate the K-S statistic
    D_n = np.max(np.abs(F_n - F))

    # Step 5: Calculate the critical value for the K-S statistic
    critical_value = stats.ksone.ppf(1 - alpha, n)

    # Step 6: Decision
    print("K-S Statistic D_n:", D_n)
    print("Critical Value:", critical_value)

    if D_n > critical_value:
        print("拒绝原假设 H0：数据不符合指定分布")
    else:
        print("不能拒绝原假设 H0：数据符合指定分布")

    # Optional: Plotting the EDF and theoretical distribution
    plt.step(sorted_data, F_n, label="Empirical Distribution Function", where="post")
    plt.plot(sorted_data, F, label="Theoretical Distribution Function", color="red")
    plt.title("Kolmogorov-Smirnov Test")
    plt.xlabel("Data")
    plt.ylabel("Cumulative Probability")
    plt.legend()
    plt.show()


# Example data
data = np.random.normal(loc=0, scale=1, size=100)  # Generate random normal data

# Perform K-S test
kolmogorov_smirnov_test(data, distribution="norm", alpha=0.05)
