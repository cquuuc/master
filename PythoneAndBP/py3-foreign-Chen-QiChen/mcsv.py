import os
from install import install
import threading
import queue
import sys

try:
    import pandas as pd
except ImportError:
    print("缺少pandas库，正在安装...")
    install("pandas")
    import pandas as pd


NUM_THREADS = 3


def process_file(file_path, output_queue):
    data = pd.read_csv(file_path)
    output_queue.put(data)


def worker(input_queue, output_queue):
    while True:
        try:
            file_path = input_queue.get(timeout=1)  # 从输入队列中获取文件路径
            process_file(file_path, output_queue)
            input_queue.task_done()
        except queue.Empty:
            break


def main(folder_path):
    input_queue = queue.Queue()
    output_queue = queue.Queue()

    # 遍历文件夹中的CSV文件，并将文件路径添加到输入队列中
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".csv"):
            file_path = os.path.join(folder_path, file_name)
            input_queue.put(file_path)

    # 创建并启动线程
    threads = []
    for _ in range(NUM_THREADS):
        thread = threading.Thread(target=worker, args=(input_queue, output_queue))
        thread.start()
        threads.append(thread)

    # 等待所有输入队列中的文件都被处理完
    input_queue.join()

    # 结束线程
    for thread in threads:
        thread.join()

    # 将结果合并为一个DataFrame
    result_df = pd.concat(list(output_queue.queue))

    # 将结果写入结果CSV文件
    result_file_path = os.path.join(folder_path, "result.csv")
    result_df.to_csv(result_file_path, index=False)

    print(f"Save in: {result_file_path}")


if __name__ == "__main__":
    folder_path = sys.argv[1]  # 从命令行获取文件夹路径
    main(folder_path)
