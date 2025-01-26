import time
import sys


def load_dictionary(filename):
    """加载字典文件并返回单词列表"""
    with open(filename, "r") as file:
        words = [line.strip() for line in file if line.strip()]  # 过滤空行
    words.sort()  # 对单词进行排序
    print(f"Total words loaded: {len(words)}")  # 打印总单词数
    print("Loaded words:", words[:10])  # 打印前10个单词
    return words


def linear_search(words, search_string):
    """线性搜索以查找以给定前缀开头的单词"""
    result = []
    search_string = search_string.lower()  # 将搜索字符串转换为小写
    for word in words:
        if word == search_string:
            print(f"Checking word: {word}")  # 打印正在检查的单词
        if word.lower().startswith(search_string):  # 检查单词是否以搜索字符串开头
            result.append(word)  # 如果匹配，添加到结果列表
    return result


def binary_search(words, search_string):
    """二分搜索以查找以给定前缀开头的单词"""
    result = []
    search_string = search_string.lower()  # 将搜索字符串转换为小写
    left, right = 0, len(words) - 1

    while left <= right:
        mid = (left + right) // 2
        print(f"Checking middle word: {words[mid]}")  # 打印中间单词

        # 如果中间单词以搜索字符串开头，添加到结果并扩展搜索
        if words[mid].lower().startswith(search_string):
            result.append(words[mid])  # 添加中间单词到结果
            # 向左扩展搜索
            for i in range(mid - 1, -1, -1):
                if words[i].lower().startswith(search_string):
                    result.append(words[i])
                else:
                    break
            # 向右扩展搜索
            for i in range(mid + 1, len(words)):
                if words[i].lower().startswith(search_string):
                    result.append(words[i])
                else:
                    break
            break
        elif words[mid].lower() < search_string:  # 如果中间单词小于搜索字符串，向右搜索
            left = mid + 1
        else:  # 如果中间单词大于搜索字符串，向左搜索
            right = mid - 1

    return result


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 dictsearch.py <dictionary_file> <search_string>")
        return

    dictionary_file = sys.argv[1]
    search_string = sys.argv[2].strip("'")  # 去掉引号
    print(f"Searching for: {search_string}")

    # 加载字典
    start_time = time.time()
    words = load_dictionary(dictionary_file)
    load_time = time.time() - start_time

    # 线性搜索
    start_time = time.time()
    linear_results = linear_search(words, search_string)
    linear_time = time.time() - start_time

    # 二分搜索
    start_time = time.time()
    binary_results = binary_search(words, search_string)
    binary_time = time.time() - start_time

    # 输出结果
    print("Linear search results:", linear_results)
    print("Linear search time:", load_time + linear_time)
    print("Binary search results:", binary_results)
    print("Binary search time:", binary_time)


if __name__ == "__main__":
    main()
