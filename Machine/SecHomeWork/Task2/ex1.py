
import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
# import kagglehub
# # Download latest version
# path = kagglehub.dataset_download("nikhil7280/student-performance-multiple-linear-regression")
# print("Path to dataset files:", path)

#创建一个随机数生成器rng，种子为1，以确保结果的可重复性。
rng = np.random.RandomState(1) 

# 生成包含50个元素的随机数组x，取值范围在0到10之间
x = 10 * rng.rand(50)

#根据x的值计算对应的正弦值，并加上一些随机噪声，生成目标变量y
y = np.sin(x) + 0.1 * rng.randn(50)

#绘制散点图，用红色表示数据点的分布。
plt.scatter(x, y, c ='red')
# plt.show()

#从sklearn库中导入线性回归模型。
from sklearn.linear_model import LinearRegression 

#创建一个线性回归模型对象，设置fit_intercept参数为True，表示模型会拟合截距。
model = LinearRegression(fit_intercept=True)

#将x转换为列向量，以符合线性回归模型的输入要求。
X = x[:, np.newaxis]

#使用x和y训练线性回归模型。
model.fit(X, y)

#生成用于测试的x值，均匀分布在x的最小值和最大值之间，共50个点。
testx = np.linspace(np.min(x),np.max(x),50)[:, np.newaxis]

#再次绘制原始数据的散点图。
plt.scatter(x, y, c ='red')

#绘制线性回归模型在测试数据上的预测结果。
plt.plot(testx,model.predict(testx))

#计算线性回归模型在训练数据上的得分。
model.score(X,y)

#打印线性回归模型的系数和截距。
# print(model.coef_,model.intercept_)

#导入多项式特征生成器。
from sklearn.preprocessing import PolynomialFeatures

#创建一个多项式特征生成器对象，指定多项式的阶数为5。
poly_reg=PolynomialFeatures(degree=5)


#使用多项式特征转换器 poly_reg 对特征矩阵 X 进行转换，生成新的特征矩阵 X_new。这个转换可以将原始特征转换为多项式特征，以便更好地拟合非线性关系。
X_new = poly_reg.fit_transform(X)


#计算了新的特征矩阵 X_new 的行列式，通过计算矩阵的行列式可以评估特征之间的相关性和共线性。
np.linalg.det(np.dot(X_new.T,X_new))

#创建了一个不带截距的线性回归模型对象 model。在这种情况下，模型不会拟合截距项。
model = LinearRegression(fit_intercept=False)

#拟合线性回归模型。这里使用了经过多项式特征转换后的特征矩阵。
model.fit(X_new, y)

#生成了一个包含50个等间距点的测试数据 testx，用于绘制模型的预测结果。
testx = np.linspace(np.min(x),np.max(x),50)[:, np.newaxis]

#制了原始数据点的散点图
plt.scatter(x, y, c ='red')

#绘制了线性回归模型在测试数据 testx 上的预测结果曲线。
#首先，对测试数据进行多项式特征转换，然后使用模型进行预测。
plt.plot(testx,model.predict(poly_reg.fit_transform(testx)))
plt.show()

#这行代码计算了线性回归模型在经过多项式特征转换后的特征矩阵 X_new 和目标变量 y 下的决定系数（R^2 分数），用来衡量模型的拟合优度。
model.score(X_new,y)
# print(model.coef_,model.intercept_)



