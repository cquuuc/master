import os
import sys


def walk_dir(directory):
    files_list = []
    total_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_size = os.stat(file_path).st_size
            files_list.append((file_path, file_size))
            total_files += 1

    files_list.sort(key=lambda x: x[1], reverse=True)

    return total_files, files_list


if __name__ == "__main__":

    directory = sys.argv[1]  # 使用相对路径加载字典文件
    print(directory)
    total_files, files_list = walk_dir(directory)

    print(f"Files: {total_files}\n")

    for file_path, file_size in files_list:
        if file_size < 1024**2:
            size_str = "{:.2f} KB".format(file_size / 1024)
        elif file_size < 1024**3:
            size_str = "{:.2f} MB".format(file_size / 1024**2)
        else:
            size_str = "{:.2f} GB".format(file_size / 1024**3)

        print(f"{size_str.rjust(15)} {file_path}")
