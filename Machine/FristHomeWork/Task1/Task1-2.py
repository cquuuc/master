import numpy as np

def Fuc(mode=0):
  ji=0
  ou=0
  x=0
  res=[[],[],[],[],[],[],[],[]]
  while x <8:
    if(x%2==1):
      ji=2**x+ji
    else:
      ou=2**x+ou
    x+=1
  # print(ji,ou)


  for index in range(0,8):
    if(index%2==mode):
      # print(index)
      res[index]=[ji]
    else:
      # print(index)
      res[index]=[ou]

  
  # print(res)
  a=np.array(res,dtype=np.uint8)
  b=np.unpackbits(a,axis=1)
  print(b,"\n")
  return b

Fuc()
Fuc(1)
# print(np.unpackbits(np.array([[170],[85],[170]],dtype=np.uint8),axis=1))