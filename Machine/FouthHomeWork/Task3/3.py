# TASK3
# Using built-in *python* capabilities, implement a simple classifier model for the data from Sec. 1 and Sec. 2. Draw conclusions about the accuracy using the *accurancy_score* metric.
# 使用内置的*python*功能，为章节1和章节2中的数据实现一个简单的分类器模型。使用*accurancy_score*指标得出关于准确性的结论。

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

IMDB_data = pd.read_csv("../Task2/IMDB_data_cleaned.csv")
