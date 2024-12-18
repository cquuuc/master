import random

# 生成一个包含1000个随机整数的数组
random_numbers = [random.randint(1, 1000) for _ in range(1000)]

# 将数组写入到文件中
with open(
    "/Users/ROG/Desktop/master_1/PythoneAndBP/py3-foreign-Chen-QiChen/numbers.txt", "w"
) as file:
    for number in random_numbers:
        file.write(str(number) + "\n")

print("随机整数数组已成功写入到 'numbers.txt' 文件中。")
