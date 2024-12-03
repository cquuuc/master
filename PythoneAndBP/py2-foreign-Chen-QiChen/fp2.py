from itertools import cycle, islice


def rotate_list(lst, positions):
    if not lst:  # 检查列表是否为空
        return lst

    # 计算实际移动的位置，避免不必要的循环
    positions = positions % len(lst)

    # 使用 cycle 和 islice 进行循环移动
    res = list(islice(cycle(lst), positions, positions + len(lst)))

    return res


# 示例用法
def rotation():
    original_list = [1, 2, 3, 4, 5]
    positions = 2  # 要移动的位置
    res_list = rotate_list(original_list, positions)

    print(f"Original list: {original_list}")
    print(f"res list (by {positions} positions): {res_list}")


# 调用演示函数
rotation()
