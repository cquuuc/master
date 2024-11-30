import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
import copy
from failName import readtsv2 
try:
  dataframe=pd.read_csv("Student.csv")   
except:
  try:
    dataframe=pd.read_csv(readtsv2('Student.csv'))
  except:
    print('err in filename')

'''yes 和 no转成数字'''
ExAct_mapping={'Yes':1,'No':0}
dataframe['Extracurricular Activities'] = dataframe['Extracurricular Activities'].map(ExAct_mapping).astype(int)

#结果Y
Y=dataframe["Performance Index"].values 

#需要删除的特征列
X = dataframe.drop(['Performance Index'],axis=1).values 

from anyResFunc1 import model
model.fit(X, Y)
print('My',model.score(X,Y))
print(model.coef_,model.intercept_)

try:
  #导入多项式特征生成器。
  from sklearn.preprocessing import PolynomialFeatures
  from sklearn.linear_model import LinearRegression
  #创建一个多项式特征生成器对象，指定多项式的阶数为5。
  poly_reg=PolynomialFeatures(5)
  X_new = poly_reg.fit_transform(X)
  np.linalg.det(np.dot(X_new.T,X_new))
  model = LinearRegression(fit_intercept=False)
  model.fit(X_new, Y)
  testx = np.linspace(np.min(X),np.max(X),50)[:, np.newaxis]
  print('多项式',model.score(X_new,Y))
  print(model.coef_,model.intercept_)
except:
  print('An exception occurred')