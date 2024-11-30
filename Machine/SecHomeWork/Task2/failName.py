import numpy as np
import numdifftools as nd
import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
def readtsv():
 # 从housing.tsv文件中读取数据
  data = pd.read_csv('housing.csv', delimiter='\t')

  # 假设housing.tsv文件包含名为longitude的列，将rng数据存储在变量rng中
  # rng = data['longitude'].values
  return data
# try:
#   print(readtsv())
# except:
#   print('法一报错')


def readtsv2(filename):
  # 创建列名列表
  columns = ''
  script_dir = os.path.dirname(os.path.abspath(__file__))
  # file = os.path.join(script_dir, 'housing.csv')  # 使用相对路径加载字典文件
  file = os.path.join(script_dir, filename)  # 使用相对路径加载字典文件
  return file
  # with open(file, 'r') as f:
    # columns=f.readline()
    # for line in f:
    #   print(line)
    
# try:
#   print(readtsv2('Fish.csv'))
# except EOFError as e:
#   print('法二报错',e)