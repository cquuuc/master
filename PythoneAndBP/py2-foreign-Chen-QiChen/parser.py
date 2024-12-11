from myqueue import Queue
import os
import sys


def Fetch(filename):
    # 根据选择使用栈或队列
    container = Queue()
    operation_count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                command = line.strip().split()
                if command[0] == "add":
                    n = int(command[1])
                    container.enqueue(n)
                    operation_count += 1
                elif command[0] == "delete":
                    if container.is_empty():
                        print(f"{operation_count} Error")
                        return
                    container.dequeue()
                    operation_count += 1

        # 如果到达这里，所有操作都成功
        if not container.is_empty():
            print(operation_count, container.size(), container.peek())
        else:
            print(
                operation_count, container.size(), "None"
            )  # 如果队列/栈为空，返回 None

    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        CDfile = os.path.join(script_dir, sys.argv[1])  # 使用相对路径加载字典文件
        Fetch(CDfile)
    except EOFError as e:
        CDfile1 = sys.argv[1]  # 使用相对路径加载字典文件
        Fetch(CDfile)
