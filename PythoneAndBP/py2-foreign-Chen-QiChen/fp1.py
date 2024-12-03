from functools import reduce


def EvensRes():
    # 示例数字列表
    num = [1, 2, 3, 4, 5, 6]

    # 使用 filter 选择偶数
    evens = filter(lambda x: x % 2 == 0, num)

    # 使用 reduce 计算偶数的乘积
    res = reduce(lambda x, y: x * y, evens, 1)  # 初始值设为 1

    print(f"The res of even num in {num} is: {res}")


# 调用函数以演示其工作
EvensRes()
