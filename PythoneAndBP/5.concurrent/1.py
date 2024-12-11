import threading
import time


def fetch_data(n):
    print(f"fetching data for {n}")
    time.sleep(5)  # 模拟I/O延迟
    print(f"finished fetching data for {n}")


if __name__ == "__main__":
    pramas = ["A", "B", "C", "D", "E"]
    threads = []
    for item in pramas:
        thread = threading.Thread(target=fetch_data, args=(item,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    print("finsh")
