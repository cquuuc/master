#使用上面获得的公式，自己在任意基础上实现回归函数（仅使用基本函数和numpy）。使用矩阵计算！
#创建一个随机数生成器rng，种子为1，以确保结果的可重复性。
import numpy as np
import matplotlib.pyplot as plt
import math

#提高拟合度就靠他
degree=3
# degree=7
# degree=15

#创建一个随机数生成器rng，种子为1，以确保结果的可重复性。
rng = np.random.RandomState(1) 
# 生成包含50个元素的随机数组x，取值范围在0到10之间
x = 10 * rng.rand(50)
#根据x的值计算对应的正弦值，并加上一些随机噪声，生成目标变量y
noise=(1/math.factorial(3))*pow(np.sin(x),5)
y=1 - np.exp(-0.3*x)+noise
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

#计算线性回归模型在训练数据上的得分。
score1=model.score(X,y)

#绘制线性回归模型在测试数据上的预测结果。
plt.plot(testx,model.predict(testx),label=f'LR1 score:{score1}')


#打印线性回归模型的系数和截距。
print('LR1:',model.coef_,model.intercept_)

#导入多项式特征生成器。
from sklearn.preprocessing import PolynomialFeatures

#创建一个多项式特征生成器对象，指定多项式的阶数为5。
poly_reg=PolynomialFeatures(degree)
X_new = poly_reg.fit_transform(X)
# print(X)
np.linalg.det(np.dot(X_new.T,X_new))
model2 = LinearRegression(fit_intercept=False)
model2.fit(X_new, y)
testx = np.linspace(np.min(x),np.max(x),50)[:, np.newaxis]
plt.scatter(x, y, c ='red')
score2=model2.score(X_new,y)
plt.plot(testx,model2.predict(poly_reg.fit_transform(testx)),label=f'LR2 score:{score2}')
print('LR2:',model2.coef_,model2.intercept_)


x = np.linspace(0, 10, 100)  # 生成 x 值
y = 1 - np.exp(-0.3*x)  # 计算对应的 y 值

plt.plot(x, y,linestyle='--', label='A class step function(1 - e^(-0.3x))')
plt.legend()  # 添加图例
plt.show()


'''
在不同的人工数据上练习你的模型和内置模型。

'''
x = rng.rand(50)
noise = rng.normal(0, 0.01, 50)
y = np.sin(3.14*x)*np.sin(3.14*x) + noise
plt.scatter(x, y, c ='red')

#将x转换为列向量，以符合线性回归模型的输入要求。
X = x[:, np.newaxis]

X_new = poly_reg.fit_transform(X)
np.linalg.det(np.dot(X_new.T,X_new))
model.fit(X_new, y)

testx = np.linspace(np.min(x),np.max(x),50)[:, np.newaxis]

plt.scatter(x, y, c ='red')
score=model.score(X_new,y)
plt.plot(testx,model.predict(poly_reg.fit_transform(testx)),label=f'LR3 score:{score}')
print('LR3:',model.coef_,model.intercept_)


x = np.linspace(0, 1, 100)  # 生成 x 值
y =  np.sin(3.14*x)*np.sin(3.14*x)  # 计算对应的 y 值

plt.plot(x, y,linestyle='--', label='sin(3.14*x)^2')
plt.legend()  # 添加图例
plt.show()
