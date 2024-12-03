import os
import sys
import pandas as pd
from functools import reduce
from itertools import groupby
from operator import itemgetter


def Fech(CDfile):
    datas = []
    for item in os.listdir(CDfile):
        data = pd.read_csv(
            f"{CDfile}/{item}", delimiter=",", skipinitialspace=True, header=None
        )
        data.columns = ["Product", "Quantity", "Amount"]  # 设置列名
        datas.append(data)
    res = pd.concat(datas, ignore_index=True)  # 合并所有数据
    return res


def aggregate(data):
    # 确保金额列为浮点数
    data["Amount"] = data["Amount"].astype(float)

    # 将数据转换为元组列表
    records = list(zip(data["Product"], data["Quantity"], data["Amount"]))

    # 按产品名称分组
    grouped = groupby(sorted(records, key=itemgetter(0)), key=itemgetter(0))

    # 查看分组结果
    # for product_name, group in grouped:
    #     print(f"Product: {product_name}")
    #     for item in group:
    #         print(f"  Quantity: {item[1]}, Amount: {item[2]}")
    # 使用 map 计算每个产品的总数量和总金额
    def calculate_totals(item):
        product_name = item[0]
        group = list(item[1])  # 将 group 转换为列表以便多次迭代
        total_quantity = sum(map(itemgetter(1), group))  # 计算总数量
        total_amount = sum(map(itemgetter(2), group))  # 计算总金额

        # 打印当前组的内容
        # print("item[1]", group, "\n")

        return (product_name, total_quantity, total_amount)

    aggregated = list(map(calculate_totals, grouped))

    return aggregated


def print_results(sorted_results):
    for product_name, total_quantity, total_amount in sorted_results:
        print(f"{product_name},{total_quantity},{total_amount:.2f}")


if __name__ == "__main__":
    try:
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            CDfile = os.path.join(script_dir, sys.argv[1])  # 使用相对路径加载字典文件
            data = Fech(CDfile)
        except:
            CDfile = sys.argv[1]  # 使用相对路径加载字典文件
            data = Fech(CDfile)

        aggregated_results = aggregate(data)
        sorted_results = sorted(
            aggregated_results, key=itemgetter(2), reverse=True
        )  # 按总金额降序排序
        print_results(sorted_results)
    except FileNotFoundError as fnf_error:
        print(f"File not found: {fnf_error}")
    except pd.errors.EmptyDataError:
        print("No data found in the file.")
    except Exception as err:
        print("An exception occurred:", err)
