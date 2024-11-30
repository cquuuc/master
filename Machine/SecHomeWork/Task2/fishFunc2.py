'''
构建模型（内置模型和您的模型）来从fish .csv文件中预测鱼的重量。尝试不同的基础，不同的特征组合，努力提高预测的准确性。
'''
import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import copy
from failName import readtsv2 
try:
  dataframe=pd.read_csv("Fish.csv")   
except:
  try:
    dataframe=pd.read_csv(readtsv2('Fish.csv'))
  except:
    print('err in filename')

def PCA_(num):
  L = dataframe.drop(["Species","Weight","Height","Width"],axis=1).values 
  from sklearn.decomposition import PCA
  # 创建一个PCA对象，指定主成分数量
  pca = PCA(n_components=num)
  # 拟合数据
  pca.fit(L)
  # 进行正交基变换
  length_pca = pca.transform(L)
  # 将PCA转换后的数据添加回原始数据中
  a=copy.copy(dataframe)#浅拷贝不影响源数据
  i = 1
  while i <= num-1:
    a[f'PCA{i}'] = length_pca[:, i]
    i += 1
  # a['PCA2'] = length_pca[:, 1]
  return a.drop(["Species","Weight","Length1","Length2","Length3"],axis=1).values 


def default():
  return dataframe.drop(["Species","Weight"],axis=1).values 

def default2():
  return dataframe.drop(["Species","Weight","Length1",],axis=1).values 
def default3():
  return dataframe.drop(["Species","Weight","Length2",],axis=1).values 
def default4():
  return dataframe.drop(["Species","Weight","Length3",],axis=1).values 
def default5():
  return dataframe.drop(["Species","Weight","Length1","Length2",],axis=1).values 
def default6():
  return dataframe.drop(["Species","Weight","Length1","Length3",],axis=1).values 
def default7():
  return dataframe.drop(["Species","Weight","Length2","Length3",],axis=1).values 

def Z():
  feature_mean=dataframe.mean(numeric_only=True)
  feature_std = dataframe.std(numeric_only=True)
  numerical_features = dataframe.select_dtypes('number').columns
  normalized_dataset = (
    dataframe[numerical_features] - feature_mean
) / feature_std
  
  mapping = {'Bream': 1, 'Roach': 10, 'Whitefish': 100, 'Parkki': 1000, 'Perch': 10000, 'Pike': 100000, 'Smelt': 1000000}
  normalized_dataset['Species'] = dataframe['Species'].map(mapping).astype(int)
  # print(normalized_dataset.head())
  # print(normalized_dataset.sample(frac=1, random_state=100))
  return normalized_dataset
  



X =PCA_(1)#0.787
X =PCA_(2)#0.797
X =default5()#0.877
X =default6()#0.881
X =default7()#0.882
X =default2()#0.883
X =default4()#0.883
X =default3()#0.88526
X =default() #0.8852867046546207
X =Z()#1.0



y = dataframe["Weight"].values 

try:
  #导入多项式特征生成器。
  from sklearn.preprocessing import PolynomialFeatures
  from sklearn.linear_model import LinearRegression
  #创建一个多项式特征生成器对象，指定多项式的阶数为5。
  poly_reg=PolynomialFeatures(5)
  X_new = poly_reg.fit_transform(X)
  np.linalg.det(np.dot(X_new.T,X_new))
  model = LinearRegression(fit_intercept=False)
  model.fit(X_new, y)
  testx = np.linspace(np.min(X),np.max(X),50)[:, np.newaxis]
  print('多项式',model.score(X_new,y))
  print(model.coef_,model.intercept_)

except:
  from sklearn.linear_model import LinearRegression
  model = LinearRegression(fit_intercept=True) 
  model.fit(X, y)
  print('线性',model.score(X,y))
  print(model.coef_,model.intercept_)
finally:
  from anyResFunc1 import model
  model.fit(X, y)
  print('My',model.score(X,y))
  print(model.coef_,model.intercept_)

