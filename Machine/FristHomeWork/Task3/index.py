import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


# def simplest_lin_regression(x,y):
#   #Matplotlib 绘制散点图，展示 x 和 y 之间的关系。
#   plt.scatter(x, y);
#   # 导入 Scikit-Learn 库中的线性回归模型,创建一个线性回归模型对象,模型会拟合截距
#   model = LinearRegression(fit_intercept=True)
#   #将 x 转换成了二维数组，以符合 Scikit-Learn 模型的输入要求
#   X = x[:, np.newaxis]
#   #调用模型的 fit 方法来拟合数据，学习模型参数。
#   model.fit(X, y)
#   #输出模型的斜率和截距。模型的拟合优度（R^2 分数），用来衡量模型对数据的拟合程度。
#   return {"a":model.coef_,"b":model.intercept_,"R^2":model.score(X,y)}


# rng = np.random
# x = 10 * rng.rand(50)
# y = 2 * x - 1 + rng.randn(50)

# print(simplest_lin_regression(x,y))


def simplest_lin_regression(x, y):
    # 绘制散点图
    plt.scatter(x, y)
    # 创建线性回归模型对象
    model = LinearRegression(fit_intercept=True)
    # 将 x 转换成二维数组
    X = x[:, np.newaxis]
    # 拟合数据
    model.fit(X, y)
    # 绘制拟合后的直线
    plt.plot(x, model.predict(X), color='r')
    # 显示图形
    plt.show()
    # 返回拟合结果
    return {"a": model.coef_, "b": model.intercept_, "R^2": model.score(X, y)}

rng = np.random
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)

print(simplest_lin_regression(x, y))
