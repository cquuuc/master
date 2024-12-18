import random
import threading
import sys

num_threads = 3  # 可以根据你的CPU核心数进行调整


def estimate_pi(num_points):
    points_inside_circle = 0
    total_points = 0

    for _ in range(num_points):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2

        if distance <= 1:
            points_inside_circle += 1
        total_points += 1

    return points_inside_circle, total_points


def main(num_points):

    # 将点的数量均匀分配给每个线程
    points_per_thread = num_points // num_threads

    # 创建线程并启动
    threads = []
    results = []
    for _ in range(num_threads):
        thread = threading.Thread(
            target=lambda: results.append(estimate_pi(points_per_thread))
        )
        threads.append(thread)
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # 汇总结果
    total_points_inside_circle = sum(result[0] for result in results)
    total_points = sum(result[1] for result in results)

    # 计算估算的圆周率
    pi_estimate = 4 * total_points_inside_circle / total_points

    print(f"Estimated PI: {pi_estimate}")


if __name__ == "__main__":
    num_points = int(sys.argv[1])  # 从命令行获取点的数量
    main(num_points)
