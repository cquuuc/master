import heapq
import sys
import os
import pandas as pd


def dijkstra(graph, start):
    distances = {city: float("infinity") for city in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_city = heapq.heappop(queue)

        if current_distance > distances[current_city]:
            continue

        for neighbor, weight in graph[current_city].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances


def main(file, start_city):
    # 尝试读取数据，支持多种分隔符
    try:
        df = pd.read_csv(
            file,
            delim_whitespace=True,
            header=None,
            names=["city1", "city2", "distance"],
            encoding="utf-8",
        )
    except ValueError:
        try:
            df = pd.read_csv(
                file,
                sep=",",
                header=None,
                names=["city1", "city2", "distance"],
                encoding="utf-8",
            )
        except ValueError:
            df = pd.read_csv(
                file,
                sep="\t",
                header=None,
                names=["city1", "city2", "distance"],
                encoding="utf-8",
            )
    # 检查并处理缺失值
    df.dropna(inplace=True)  # 删除包含 NaN 的行

    # 构建图
    graph = {}
    for _, row in df.iterrows():
        city1, city2, distance = row["city1"], row["city2"], row["distance"]
        distance = int(distance)  # 确保 distance 是整数
        if city1 not in graph:
            graph[city1] = {}
        if city2 not in graph:
            graph[city2] = {}
        graph[city1][city2] = distance
        graph[city2][city1] = distance

    # 调试信息：打印图的内容
    print("Graph:", graph)

    if start_city not in graph:
        print(f"Error: '{start_city}' not found in the graph.")
        return

    distances = dijkstra(graph, start_city)
    nearest_cities = sorted(distances.items(), key=lambda x: x[1])[:5]
    farthest_cities = sorted(distances.items(), key=lambda x: x[1], reverse=True)[:5]

    print("Top 5 nearest cities:")
    for city, distance in nearest_cities:
        print(f"('{city}', {distance})")

    print("\nTop 5 distant cities:")
    for city, distance in farthest_cities:
        print(f"('{city}', {distance})")


if __name__ == "__main__":
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file = os.path.join(script_dir, sys.argv[1])  # 使用相对路径加载字典文件
    except EOFError as e:
        file = sys.argv[1]  # 使用相对路径加载字典文件
    start_city = sys.argv[2]
    main(file, start_city)
