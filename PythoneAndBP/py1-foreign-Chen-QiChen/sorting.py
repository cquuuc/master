import random
import time
import numpy as np
import sys


# 选择排序
def selection_sort(lst):
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]


# 冒泡排序
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


# 插入排序
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key


# 快速排序
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 归并排序
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Python内置排序
def python_sort(lst):
    return sorted(lst)


if __name__ == "__main__":
    n, m, k = map(int, sys.argv[1:4])

    random_lst = [random.randint(1, m) for _ in range(n)]

    # 复制列表以便每种排序方法使用相同的输入
    lst_copy = random_lst.copy()
    Fuc = [
        selection_sort,
        bubble_sort,
        insertion_sort,
        quick_sort,
        merge_sort,
        python_sort,
    ]

    for fuc in Fuc:
        start_time = time.time()
        fuc(lst_copy)
        end_time = time.time()
        # print(fuc.__name__)
        print("{:.15f}".format(end_time - start_time))
        print("{:.15f} {}".format(time.time() - start_time, lst_copy[-10:]))
