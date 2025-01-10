# 1. 研究具有源数据特征的点工作示例。
# 2. 在使用文档和示例之后，为著名的[titanik数据集]（https://www.kaggle.com/c/titanic/data）以及[操作符]（https://www.kaggle.com/datasets/mnassrib/telecom-churn-datasets）数据选择和准备特征
# + 2.1可视化的功能。确定它们的类型。
# 在必要时删除异常数据（使用最简单的z-score和IQR方法）。
# + 2.3使用描述性统计和相关性识别重要特征。
# + 2.4根据自己的判断填空并使用数据。
# + 2.5将准备好的数据集保存到新的csv文件中。
# [https://scikit-learn.org/stable/modules/preprocessing.html] (https://scikit-learn.org/stable/modules/preprocessing.html)
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score, roc_curve
import os


titanic_train = pd.read_csv("titanic/train.csv")
titanic_test = pd.read_csv("titanic/test.csv")
titanic_test_Survived = pd.read_csv("titanic/gender_submission.csv")
archive_train = pd.read_csv("archive/churn-bigml-20.csv")
archive_test = pd.read_csv("archive/churn-bigml-80.csv")


sex_map = {"male": 1, "female": 0}
cabin_map = titanic_train["Cabin"].notna().astype(int)

titanic_test["Cabin_Indicator"] = cabin_map
titanic_test["Sex_Indicator"] = titanic_train["Sex"].map(sex_map)
titanic_train["Cabin_Indicator"] = cabin_map
titanic_train["Sex_Indicator"] = titanic_train["Sex"].map(sex_map)


# 定义 Andrews 曲线函数
def andrews_curve(x, theta):
    curve = list()
    for th in theta:
        x1 = x[0] / np.sqrt(2)
        x2 = x[1] * np.sin(th)
        x3 = x[2] * np.cos(th)
        x4 = x[3] * np.sin(2.0 * th)
        x5 = x[4] * np.sin(th)  # 使用 Cabin_Indicator
        curve.append(x1 + x2 + x3 + x4 + x5)
    return curve


# # 设置参数
# accuracy = 1000
# samples = titanic_train[["Age", "Fare", "Pclass", "Survived", "Cabin_Indicator"]].values
# theta = np.linspace(-np.pi, np.pi, accuracy)

# # 绘制 Andrews 曲线
# plt.figure(figsize=(12, 6))
# for s in samples[:5]:  # 选择前 5 个样本
#     plt.plot(theta, andrews_curve(s, theta), "r")

# for s in samples[5:10]:  # 选择接下来的 5 个样本
#     plt.plot(theta, andrews_curve(s, theta), "g")

# plt.xlim(-np.pi, np.pi)
# plt.title("Andrews Curves for Titanic Dataset with Cabin Indicator")
# plt.xlabel("Theta")
# plt.ylabel("Curve Value")
# plt.show()
