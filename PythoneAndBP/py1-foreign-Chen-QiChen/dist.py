#找出地球上两点之间的最短距离。这些点由它们的纬度和经度指定（𝜙1 λ1 𝜙2 λ2）。 r（地球半径）取为 6378.137
#计算明斯克和北京之间距离的示例。
#％python3 dist.py 53.66 23.99 39.90 116.41
# 6698

import sys
import numpy as np
import math


def dist(array):
  #固定半径
  EarthR=6378.137
  #解构赋值
  [Fai1,Lamna1,Fai2,Lamna2]=array

  DetaLamna=math.radians(abs(Lamna1-Lamna2))
  Fai1=math.radians(Fai1)
  Lamna1=math.radians(Lamna1)
  Fai2=math.radians(Fai2)
  Lamna2=math.radians(Lamna2)

  sin_=math.sin(DetaLamna)
  sin1=math.sin(Fai1)
  sin2=math.sin(Fai2)
  cos_=math.cos(DetaLamna)
  cos1=math.cos(Fai1)
  cos2=math.cos(Fai2)

  upper=((cos2*sin_)**2+(cos1*sin2-sin1*cos2*cos_)**2)
  lower=sin1*sin2+cos1*cos2*cos_
  res=round(math.atan2(math.sqrt(upper) ,lower) *EarthR) 
  print(res)
  return res



if __name__ == "__main__":
    # 从命令行参数中获取除脚本名外的所有参数
    input_str = sys.argv[1:][0]
    # 使用空格分割字符串，并转换为浮点数数组
    result_array = np.array(input_str.split(), dtype=float)
    # print(result_array)
    dist(result_array)