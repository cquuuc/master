import threading
import sys
from install import install

try:
    import pandas as pd
except ImportError:
    print("缺少pandas库，正在安装...")
    install("pandas")
    import pandas as pd


# 定义常量NUM_THREADS来表示线程数
NUM_THREADS = 3
total_even = 0
total_odd = 0
count = 0


def fetch(path):
    data = pd.read_csv(path, header=None)
    return data


def worker(chunk):
    global total_even, total_odd, count  # 声明使用全局变量
    count = 1 + count
    even_count = sum(1 for number in chunk[0] if number % 2 == 0)  # 假设数据在第一列
    odd_count = len(chunk) - even_count
    total_even = even_count + total_even
    total_odd = odd_count + total_odd
    print(f"处理结果{count} - 偶数数量: {even_count}, 奇数数量: {odd_count}")


def main(file_path):
    # 从命令行获取文件路径
    data = fetch(file_path)

    # 根据线程数将数据分成几部分
    chunk_size = len(data) // NUM_THREADS
    chunks = [data[i : i + chunk_size] for i in range(0, len(data), chunk_size)]

    # 创建线程并启动
    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=worker, args=(chunk,))
        threads.append(thread)
        thread.start()

    # 确保所有线程都已退出
    for thread in threads:
        thread.join()

    print("所有线程处理完成。")
    print(f"even: {total_even}, old: {total_odd}")


if __name__ == "__main__":
    main(sys.argv[1])  # 直接调用主函数
