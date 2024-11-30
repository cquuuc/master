'''
1解析输入参数，得到硬币集合和要找零的金额。
2编写贪心算法和动态规划算法来计算最少硬币数量。
3比较两种算法得到的结果，并输出最少硬币数量。
'''
import sys

def greedy(coins, amount):
    coins.sort(reverse=True)
    num = 0
    for coin in coins:
        num += amount // coin
        amount %= coin
    return num if amount == 0 else float('inf')

def dynamic(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else float('inf')

if __name__ == "__main__":
    coins = list(map(int, sys.argv[1].split(',')))
    amount = int(sys.argv[2])

    res1 = greedy(coins, amount)
    res2 = dynamic(coins, amount)

    print(f"greedy: {res1}")
    print(f"dynamic: {res2}")
