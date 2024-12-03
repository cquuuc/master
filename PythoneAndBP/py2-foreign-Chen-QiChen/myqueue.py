class Queue:
    def __init__(this):
        this.items = []  # 用于存储队列元素
        this.enqueue_count = 0  # 记录入队次数
        this.dequeue_count = 0  # 记录出队次数

    def enqueue(this, item):
        """将元素添加到队列的末尾"""
        this.items.append(item)
        this.enqueue_count += 1  # 增加入队计数

    def dequeue(this):
        """从队列的前面移除并返回元素"""
        if this.is_empty():
            raise IndexError("dequeue from an empty queue")
        this.dequeue_count += 1  # 增加出队计数
        return this.items.pop(0)  # 移除并返回第一个元素

    def peek(this):
        """返回队列的第一个元素而不移除它"""
        if this.is_empty():
            raise IndexError("peek from an empty queue")
        return this.items[0]  # 返回第一个元素

    def is_empty(this):
        """检查队列是否为空"""
        return len(this.items) == 0

    @property
    def size(this):
        """返回当前队列的大小"""
        return len(this.items)

    def get_enqueue_count(this):
        """返回入队次数"""
        return this.enqueue_count

    def get_dequeue_count(this):
        """返回出队次数"""
        return this.dequeue_count


# 示例用法
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(f"size: {queue.size}")  # 输出: 当前队列大小: 3
    print(f"dequeue: {queue.dequeue()}")  # 输出: 出队元素: 1
    print(f"size: {queue.size}")  # 输出: 当前队列大小: 2
    print(f"get_enqueue_count: {queue.get_enqueue_count()}")  # 输出: 入队次数: 3
    print(f"get_dequeue_count: {queue.get_dequeue_count()}")  # 输出: 出队次数: 1
