import numpy as np

setting={"x0":0,
         "x1":1,
         "y0":0,
         "y1":1}

def Task1_3(_setting,_num_point,Beginner=1):
  x=np.linspace(_setting["x0"],_setting["x1"],_num_point)
  y=np.linspace(_setting["y0"],_setting["y1"],_num_point)
  
  # X,Y=np.meshgrid(x,y)
  # res=np.concatenate([x,y],axis=1)

  if Beginner==1:
    res=np.vstack([x,y])
  else:
   [res]=np.random.standard_normal(size=(1,2,_num_point))
   res[res<0]= -res[res<0]#负的取正
  
  

  return res

a=Task1_3(setting,4)
b=Task1_3(setting,4,0)
print(a,'\n\n',b)