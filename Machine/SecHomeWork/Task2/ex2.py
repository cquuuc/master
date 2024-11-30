import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
from failName import readtsv2 
try:
  dataframe=pd.read_csv("Fish.csv")   
except:
  try:
    dataframe=pd.read_csv(readtsv2('Fish.csv'))
  except:
    print('err in filename')

print(dataframe.head())

#从数据框中删除了"Species"和"Weight"两列，
#并将剩余的特征列转换为一个NumPy数组。这些特征将用作线性回归模型的输入。
#X是特征矩阵，包含了除了"Species"和"Weight"之外的所有特征列。
X = dataframe.drop(["Species","Weight"],axis=1).values 

# X = dataframe.drop(["Species"],axis=1).values 
#数据框中选择了目标变量"Weight"，并将其转换为一个NumPy数组。这将作为线性回归模型的目标输出。
#y是目标变量，即我们要预测的"Weight"列
y = dataframe["Weight"].values 
# print(X,y)

#从sklearn库中导入线性回归模型。
from sklearn.linear_model import LinearRegression,Ridge,RidgeCV,OrthogonalMatchingPursuit,BayesianRidge,TweedieRegressor,HuberRegressor

#创建了一个线性回归模型对象，并指定 fit_intercept=True，表示模型会拟合截距
model = LinearRegression(fit_intercept=True) 
# model = Ridge(fit_intercept=True) 
# model = RidgeCV(fit_intercept=True) 
# model = OrthogonalMatchingPursuit(fit_intercept=True) 
# model = BayesianRidge()
# model = TweedieRegressor()
# model = HuberRegressor()

 



#使用特征矩阵 X 和目标变量 y 来拟合线性回归模型
model.fit(X, y)
# print(X)
# print(y)

#计算了线性回归模型在给定特征矩阵 X 和目标变量 y 下的决定系数（R^2 分数），用来衡量模型的拟合优度。
print(model.score(X,y))

#输出了线性回归模型的系数（coef_）和截距（intercept_）。
print(model.coef_,model.intercept_)