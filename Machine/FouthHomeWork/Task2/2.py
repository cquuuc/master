# 1. 研究上面描述的使用文本数据集的示例。
# 2. 为进一步的工作准备一个电影评论的文本数据集。[Imdb - news]（https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews）。
# + 2.1使用*TfidfVectorizer*的内置功能。
# + 2.2通过自己实现模拟。
# + 2.3将准备好的数据集保存到新的csv文件中。
# [https://www.geeksforgeeks.org/understanding-tf-idf-term-frequency-inverse-document-frequency/] (https://www.geeksforgeeks.org/understanding-tf-idf-term-frequency-inverse-document-frequency/)
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


IMDB_data = pd.read_csv("IMDB Dataset.csv")
