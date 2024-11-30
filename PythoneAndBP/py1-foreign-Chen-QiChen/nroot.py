import sys

# 递归二分查找方法计算 k 次根
def recursive_binary_search(n, k, eps, low, high, steps=0):
    mid = (low + high) / 2
    val = mid ** k
    if abs(val - n) <= eps:  # 如果误差在允许范围内，返回结果
        return mid, steps
    if val < n:
        return recursive_binary_search(n, k, eps, mid, high, steps+1)  # 在右半边继续查找
    else:
        return recursive_binary_search(n, k, eps, low, mid, steps+1)  # 在左半边继续查找

# 牛顿法计算 k 次根
def newtons_method(n, k, eps):
    x = n / 2
    steps = 0
    # eps=eps*2
    while True:
        x_next = x - (x**k - n) / (k * x**(k-1) )  # 牛顿法迭代公式
        if abs(x_next - x) <= eps:  # 如果误差在允许范围内，返回结果
            return x_next, steps
        x = x_next
        steps += 1

# 主函数
def main(n=2, k=2, eps=0.01):
    result, steps = recursive_binary_search(n, k, eps, 0, n)
    print(steps,result)


    result, steps = newtons_method(n, k, eps)
    print(steps,result)


if __name__ == "__main__":
    if sys.argv[1:]:
      n = float(sys.argv[1])
      k = float(sys.argv[2])
      eps = float(sys.argv[3])
      main(n,k,eps)
    else :

      main()
