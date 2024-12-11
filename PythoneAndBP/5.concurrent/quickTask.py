class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class Order:
    count = 0

    def __init__(self):
        self.items = {}
        Order.count += 1

    def __str__(self):
        return ", ".join(f"{item}: {quantity}" for item, quantity in self.items.items())

    def _add(self, item, quantity):
        self.items[item] = quantity

    @classmethod
    def _count(cls):
        print(Order.count)


banana = Product("banana", "2")
apple = Product("apple", "3")

ord = Order()
ord._add(banana, 7)
ord._add(apple, 14)
print(ord)

ord._count()
