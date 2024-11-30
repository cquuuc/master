import heapq
import sys
import os

def dijkstra(graph, start):
    distances = {city: float('infinity') for city in graph}
    distances[start] = 0
    queue = [(0, start)]

    while queue:
        current_distance, current_city = heapq.heappop(queue)

        if current_distance > distances[current_city]:
            continue
        # print(current_city='Minsk')
        # print(graph)
        # print(type(current_city)==type('Minsk') )
        # for neighbor, weight in graph[current_city].items():
        for neighbor, weight in graph['Minsk'].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

def main(file, start_city):
    graph = {}
    with open(file, 'r') as f:
        for line in f:
            data = line.strip().split('    ')
            if len(data) != 3:
                # print(f"Issue with line: {line}")
                continue
            city1, city2, distance = data
            # print(city1, city2, distance,data)
            distance = int(distance)
            if city1 not in graph:
                graph[city1] = {}
            if city2 not in graph:
                graph[city2] = {}
            graph[city1][city2] = distance
            graph[city2][city1] = distance

    # print(graph)
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
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file = os.path.join(script_dir, sys.argv[1])  # 使用相对路径加载字典文件
    start_city = sys.argv[2]
    # print(start_city)
    main(file, start_city)
