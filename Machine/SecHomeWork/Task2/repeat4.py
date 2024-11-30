import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
import plotly.express as px
import keras
import pandas as pd
import sys
import os
import copy
from failName import readtsv2

file_number = 2

# 设置Pandas DataFrame 或 Series 在显示时最多显示的行数为 10。这在处理大型数据集时很有用，可以确保输出不会太长，方便查看数据的一部分而不是整个数据集。
pd.options.display.max_rows = 10

# 设置Pandas 显示浮点数时的格式。在这里，"{:.1f}".format 表示浮点数将以一位小数的格式显示。这样可以控制浮点数的显示精度，使输出更易读。
pd.options.display.float_format = "{:.1f}".format


def feachData(index):
    filelist = ["Fish.csv", "Student.csv", "housing.csv"]
    Y = ["Weight", "Performance Index", "median_house_value"]
    careful = [
        [
            "Species",
            {
                "Bream": 1,
                "Roach": 10,
                "Whitefish": 100,
                "Parkki": 1000,
                "Perch": 10000,
                "Pike": 100000,
                "Smelt": 1000000,
            },
        ],
        ["Extracurricular Activities", {"Yes": 1, "No": 0}],
        [
            "ocean_proximity",
            {
                "INLAND": 1,
                "NEAR BAY": 10,
                "NEAR OCEAN": 11,
                "<1H OCEAN": 100,
                "ISLAND": 101,
            },
        ],
    ]
    print(f"{filelist[index]}")
    try:
        dataframe = pd.read_csv(f"{filelist[index]}")
    except:
        dataframe = pd.read_csv(readtsv2(f"{filelist[index]}"))
    if file_number == 2:
        missing_bedrooms = dataframe[dataframe["total_bedrooms"].isnull()]
        dataframe = dataframe.drop(missing_bedrooms.index)

    return {
        "col": dataframe.columns,
        "data": dataframe,
        "Y": Y[index],
        "NeedDeal": careful[index],
    }


res = feachData(file_number)
data_col = [*res.get("col")]
data = res.get("data")
data.describe()
Y_col = res.get("Y")
Y = data[Y_col]


# 使用 Plotly Express 绘制散点图
fig = px.scatter_matrix(data)
# 显示图表
# fig.show()

# px.scatter_3d(
#     data,
#     x=data_col[1],
#     y=data_col[2],
#     z=data_col[3],
#     color="Class",
# ).show()

if file_number == 2:
    missing_bedrooms = data[data[res.get("NeedDeal")[0]].isnull()]
    data = data.drop(missing_bedrooms.index)


# *Z 分数规范化*
def Z(_data, _NeedDeal):
    feature_mean = _data.mean(numeric_only=True)
    feature_std = _data.std(numeric_only=True)
    numerical_features = _data.select_dtypes("number").columns
    normalized_dataset = (_data[numerical_features] - feature_mean) / feature_std
    mapping = _NeedDeal[1]
    normalized_dataset[_NeedDeal[0]] = _data[_NeedDeal[0]].map(mapping)
    return normalized_dataset


X = Z(data, res.get("NeedDeal")).drop(
    [Y_col],
    axis=1,
)


def train(X, Y, _NeedDeal):
    # 开始训练
    # 为了使实验可重复，我们设置了随机数生成器的种子。这意味着每次运行 colab 时，数据的打乱顺序、随机权重初始化的值等都将相同。
    keras.utils.set_random_seed(42)
    # print(X.sample(10))

    # # 在第80和90个百分位数处创建指数
    # number_samples = len(X)  # 计算规范化数据集中的样本数量。
    # index_80th = round(number_samples * 0.8)  # 算了第80个百分位数的索引位置
    # index_90th = index_80th + round(
    #     number_samples * 0.1
    # )  # 计算了第90个百分位数的索引位置。

    # 以。8,.1,.1分割为训练，验证和测试
    X = X.drop(columns=[_NeedDeal[0]])
    # X = X.sample(frac=1, random_state=100)
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_squared_error

    # print(X)
    # print(Y)
    X_train, X_test, y_train, y_test = train_test_split(
        X, Y, test_size=0.2, random_state=42
    )
    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size=0.25, random_state=42
    )

    from sklearn.linear_model import LinearRegression

    model = LinearRegression()
    # 训练模型
    model.fit(X_train, y_train)
    # 在验证集上进行预测
    y_val_pred = model.predict(X_val)
    # 在测试集上进行预测
    y_test_pred = model.predict(X_test)
    # 计算均方误差（Mean Squared Error）
    val_mse = mean_squared_error(y_val, y_val_pred)
    test_mse = mean_squared_error(y_test, y_test_pred)
    # 打印均方误差
    print("验证集均方误差 val_mse:", val_mse)
    print("测试集均方误差 test_mse:", test_mse)
    print("score:", model.score(X, Y))
    print(model.coef_, model.intercept_)


train(X, Y, res.get("NeedDeal"))
