import random
from concurrent.futures import ProcessPoolExecutor
import sys


def doSome(chunk):
    even_count = sum(1 for number in chunk if number % 2 == 0)
    odd_count = len(chunk) - even_count
    return even_count, odd_count


def work(size):
    # 设置进程数量
    num_processes = 3  # 可以根据你的CPU核心数进行调整

    # 生成随机整数数组
    data_size = size  # 数组大小
    data = [random.randint(1, 100) for _ in range(data_size)]

    # 将数据分块
    chunk_size = data_size // num_processes
    chunks = [data[i : i + chunk_size] for i in range(0, data_size, chunk_size)]

    # 使用ProcessPoolExecutor进行并行处理
    with ProcessPoolExecutor(max_workers=num_processes) as executor:  # 修正这里
        results = list(executor.map(doSome, chunks))

    # 处理结果
    total_even = sum(result[0] for result in results)
    total_odd = sum(result[1] for result in results)

    print(f"even: {total_even}, old: {total_odd}")


if __name__ == "__main__":
    size = int(sys.argv[1])
    work(size)
