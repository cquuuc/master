import sys
import os
import pandas as pd
from collections import deque


def Render(file):
    graph = {}
    # 使用制表符作为分隔符
    df = pd.read_csv(
        file, sep="\t", header=None, names=["actor", "movie"], encoding="utf-8"
    )
    # 检查数据框的内容
    # print("DataFrame contents:")
    # print(df.head())  # 打印前几行数
    for _, row in df.iterrows():
        actor, movie = row["actor"], row["movie"]
        if actor not in graph:
            graph[actor] = set()
        graph[actor].add(movie)
    return graph


def bfs(graph, start, end):
    queue = deque([(start, [start])])  # 存储当前演员和路径
    visited = set()  # 存储已访问的演员

    while queue:
        actor, path = queue.popleft()  # 从队列中取出一个演员和路径
        if actor == end:  # 如果找到了目标演员
            return path  # 返回路径
        visited.add(actor)  # 标记当前演员为已访问
        for movie in graph[actor]:  # 遍历当前演员参与的电影
            for neighbor in graph:  # 遍历所有演员
                if (
                    movie in graph[neighbor] and neighbor not in visited
                ):  # 如果邻居演员参与了同一部电影且未被访问
                    new_path = path + [neighbor]  # 更新路径
                    queue.append((neighbor, new_path))  # 将邻居演员和新路径加入队列
    return None  # 如果没有找到连接，返回 None


def print_common_elements(arr1, arr2):
    set1 = set(arr1)
    res = []
    for element in arr2:
        if element in set1:
            res.append(element)
    return res


if __name__ == "__main__":
    actor1 = sys.argv[2]
    actor2 = sys.argv[3]
    # print("演员", actor1)
    # print("演员", actor2)
    file = sys.argv[1]  # 使用相对路径加载字典文件
    graph = Render(file)
    path = bfs(graph, actor1, actor2)

    if path:
        distance = len(path) - 1
        print(f"Distance: {distance}")
        for i in range(len(path) - 1):
            in_what = print_common_elements(graph[path[i]], graph[path[i + 1]])
            print(f"{path[i]} was with {path[i + 1]} in {in_what}")
    else:
        print("No connection found.")
