import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import copy
from failName import readtsv2

try:
    dataframe = pd.read_csv("housing.csv")
except:
    try:
        dataframe = pd.read_csv(readtsv2("housing.csv"))
    except:
        print("err in filename")


# content_list = dataframe['ocean_proximity'].unique().tolist()
# print(content_list)
def Z(data):
    feature_mean = data.mean(numeric_only=True)
    feature_std = data.std(numeric_only=True)
    numerical_features = data.select_dtypes("number").columns
    normalized_dataset = (data[numerical_features] - feature_mean) / feature_std
    return normalized_dataset


def dataMake(data):
    ocean_proximity_mapping = {
        "INLAND": 1,
        "NEAR BAY": 10,
        "NEAR OCEAN": 100,
        "<1H OCEAN": 1000,
        "ISLAND": 10000,
    }
    labs = [
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income",
        "ocean_proximity",
        "median_house_value",
    ]
    for lab in labs:
        missing_bedrooms = data[data[lab].isnull()]
        print(missing_bedrooms.index)
        data = data.drop(missing_bedrooms.index)
    data["ocean_proximity"] = data["ocean_proximity"].map(ocean_proximity_mapping)
    return data


# dataframe=dataMake(dataframe)
dataframe = Z(dataMake(dataframe))
print(dataframe)

# 结果Y
Y = dataframe["median_house_value"].values
dataframe.to_excel("output.xlsx", index=False)
# 需要删除的特征列
X = dataframe.drop(["median_house_value"], axis=1).values
from anyResFunc1 import model

model.fit(X, Y)
print("My1", model.score(X, Y))
print(model.coef_, model.intercept_)

try:
    # 导入多项式特征生成器。
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression

    # 创建一个多项式特征生成器对象，指定多项式的阶数为5。
    poly_reg = PolynomialFeatures(5)
    X_new = poly_reg.fit_transform(X)
    np.linalg.det(np.dot(X_new.T, X_new))
    model = LinearRegression(fit_intercept=False)
    model.fit(X_new, Y)
    testx = np.linspace(np.min(X), np.max(X), 50)[:, np.newaxis]
    print("多项式", model.score(X_new, Y))
    print(model.coef_, model.intercept_)
except:
    print("An exception occurred")
