import time
import os
import sys


# 加载字典文件的函数
def load_dictionary(file_name):
    # 打开文件并逐行读取单词，存储在列表中
    with open(file_name, "r", encoding="utf-8") as file:
        words = [line.strip() for line in file]
    return words


# 线性搜索函数
def linear_search(words, search_string):
    result = []
    # 逐个单词进行线性搜索，找到以搜索字符串开头的单词
    for word in words:
        if word.startswith(search_string):
            result.append(word)
    return result


# 二分搜索函数
def binary_search(words, search_string):
    result = []
    left, right = 0, len(words) - 1
    # 二分搜索
    while left <= right:
        mid = (left + right) // 2
        if words[mid].startswith(search_string):
            # 找到以搜索字符串开头的单词后，向左右两侧扩展搜索
            result.append(words[mid])
            # 向左继续搜索
            for i in range(mid - 1, -1, -1):
                if words[i].startswith(search_string):
                    result.append(words[i])
                else:
                    break
            # 向右继续搜索
            for i in range(mid + 1, len(words)):
                if words[i].startswith(search_string):
                    result.append(words[i])
                else:
                    break
            break
        elif words[mid].startswith(search_string):
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == "__main__":

    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = os.path.join(script_dir, sys.argv[1])  # 使用相对路径加载字典文件
    except EOFError as e:
        file_name = sys.argv[1]  # 使用相对路径加载字典文件
    search_string = sys.argv[2]

    # 加载字典
    words = load_dictionary(file_name)
    print(words)
    Fuc = [linear_search, binary_search]
    for fuc in Fuc:
        start_time = time.perf_counter()
        res = fuc(words, search_string)
        d_time = time.perf_counter() - start_time
        print(d_time, res)
