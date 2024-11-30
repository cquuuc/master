# 1. Using the built-in functions of the sklearn package, implement small programs that model linear regression with L1 or L2 regularization on artificial data. Draw conclusions about the behavior of weight coefficients depending on a different number of features, including polynomial ones.
# 2. How does regularization affect the quality metrics of models?
# 3. What problems did you encounter when using the formula for calculating regression weights from LR2? Can they be solved by regularization? Using matrices, show an example of the algebraic meaning of regularization.
# 4. Modify your own function for finding regression weights from LR2 so that it corresponds to the loss function L2 - regularization. The analytical solution to the optimization problem was obtained in the lecture. Compare the results of your function with the built-in one.
"""

1. 使用sklearn包的内置函数，实现对人工数据进行L1或L2正则化的线性回归建模的小程序。根据不同数量的特征（包括多项式特征）得出关于权重系数行为的结论。

2. 正则化如何影响模型的质量度量？
  训练误差（Training Error）：正则化通常会增加模型的训练误差。这是因为正则化引入了对模型复杂性的惩罚，迫使模型更加简单，从而减少过拟合的风险。因此，正则化可以导致模型在训练数据上的拟合程度降低，训练误差相对增加。

  测试误差（Test Error）：正则化的目标是减少模型在未见过的测试数据上的误差。通过控制模型的复杂性，正则化可以帮助模型更好地泛化到新的数据。因此，正则化通常会减少模型的测试误差，提高模型的预测性能。

  方差（Variance）和偏差（Bias）：正则化可以帮助减少模型的方差，即模型对训练数据的变动敏感程度。通过限制模型的复杂性，正则化可以减少模型在训练数据中的波动，从而降低方差。然而，如果正则化过度，可能会增加模型的偏差，即模型对真实数据的拟合程度降低。

  特征选择：L1 正则化（Lasso）倾向于产生稀疏权重，即将某些特征的权重调整为零。这可以用于特征选择，即自动选择对目标变量有更强预测能力的特征。通过特征选择，可以减少模型的复杂性，提高模型的解释能力和泛化性能。

3. 在使用从LR2计算回归权重的公式时，您遇到了哪些问题？它们可以通过正则化来解决吗？利用矩阵，给出正则化的代数意义的一个例子。

4. 修改从LR2中找到回归权重的函数，使其对应于损失函数L2 -正则化。在讲座中得到了优化问题的解析解。将您的函数的结果与内置函数的结果进行比较。

"""
