import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
import pandas as pd

"""
1. Study in detail the formulas obtained above. Practice deriving them yourself.
2. Get any 2 more formulas for similar matrix or vector differentiation. Briefly summarize the derivation of the formulas in the document.
3. Check the validity of your formulas using the built-in functions of the numdifftools package.
1. 详细研究了上述公式。自己练习推导它们。
2. 求任意两个类似矩阵或向量微分的公式。简要总结文档中公式的推导过程。
3. 使用numdifftools包的内置函数检查公式的有效性。
"""
# 生成随机矩阵
A = np.random.randint(5, size=(10, 10))
B = np.random.randint(5, size=(10, 10))
C = np.random.randint(5, size=(10, 10))


def func(A):
    return np.trace(np.dot(np.dot(A, B), C))


# 计算函数func在x0处的梯度
try:
    grad = nd.Gradient(func)(A)
    res = B.T @ C
    print("func's grad in A：", grad)
    print("res", res)
except Exception as e:
    print("f1 erro")


# 设置维度
n = 5
# 列向量 a
[a] = np.random.rand(n).reshape(1, -1)


# 定义标量函数
def f(X):
    return np.dot(a, X)


try:
    # 生成一个随机列向量 X
    [X] = np.random.rand(n).reshape(1, -1)
    # 使用Numdifftools计算梯度
    vector_grad = nd.Gradient(f)(X)

    print("vector grad：", vector_grad)
    print("res", a)
except:
    print("f ERRO")
