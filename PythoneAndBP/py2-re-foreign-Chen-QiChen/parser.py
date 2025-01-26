from myqueue import Queue
import os
import sys


def Fetch(filename):
    container = Queue()
    operation_count = 0

    try:
        with open(filename, "r") as file:
            for line in file:
                command = line.strip().split()
                print(f"Command: {command}")  # 打印当前命令
                if not command:
                    continue  # 忽略空行
                if command[0] == "add":
                    if len(command) != 2:
                        print("Invalid command format for add.")
                        continue
                    try:
                        n = int(command[1])
                        container.enqueue(n)
                        operation_count += 1
                        print(
                            f"Added: {n}, Queue size: {container.size}"
                        )  # 打印添加后的队列大小
                    except ValueError:
                        print(f"Invalid number: {command[1]}")
                elif command[0] == "delete":
                    if container.is_empty():
                        print(
                            f"{operation_count} Error: Cannot delete from an empty queue."
                        )
                        continue
                    removed_item = container.dequeue()
                    operation_count += 1
                    print(
                        f"Removed: {removed_item}, Queue size: {container.size}"
                    )  # 打印移除后的队列大小
                else:
                    print(f"Unknown command: {command[0]}")

        if not container.is_empty():
            print(operation_count, container.size, container.peek())
        else:
            print(operation_count, container.size, "None")

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
