import sys
import os
from collections import deque

def Render(file):
    graph = {}
    with open(file, 'r') as f:
        for line in f:
            data = line.strip().split('    ')
            if len(data) != 2:
                # print(line,data)
                continue
            actor, movie = data
            if actor not in graph:
                graph[actor] = set()
            graph[actor].add(movie)
    print(graph)
    return graph


def bfs(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        actor, path = queue.popleft()
        if actor == end:
            return path
        visited.add(actor)
        for neighbor in graph.keys():
            if neighbor not in visited:
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return None

def print_common_elements(arr1, arr2):
    set1 = set(arr1)
    res=[]
    for element in arr2:
        if element in set1:
            # print(element)
            res.append(element)
    return res



if __name__ == "__main__":
    # file = sys.argv[1]
    actor1 = sys.argv[2]
    actor2 = sys.argv[3]

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(script_dir, sys.argv[1])  # 使用相对路径加载字典文件

    graph = Render(file)
    path = bfs(graph, actor1, actor2)

    if path:
        distance = len(path) - 1
        print(f"Distance: {distance}")
        for i in range(len(path) - 1):
            in_what=print_common_elements(graph[path[i]],graph[path[i+1]])
            print(f"{path[i]} was with {path[i+1]} in {in_what}")
            
    else:

        print("No connection found.")
