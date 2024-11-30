import numpy as np
# print(np.__version__)

import sys
# print(sys.version)

# print(np.arctan(10))

# grid=np.arange(1,10).reshape(3,3)
# grid=np.arange(1,10).reshape(3,2) //erro
# print(grid)
x=np.array([1,2,3])
# x.reshape((1,3))
# x.reshape((3,1))
# x[np.newaxis,:]
# print(x)
y=np.array([3,2,1])
z=np.array([99,99,99])
NewGrid=np.concatenate([x,y,z])
# print(NewGrid)
gride1=np.array([[1,2,3],[4,5,6]])
gride2=np.zeros((2,3))
print(gride2)
# print(gride1)
NewGrid1=np.concatenate([gride1,gride2])
NewGrid2=np.concatenate([gride1,gride2],axis=1)
# print(NewGrid1)
# print(NewGrid2)
NewGrid3=np.vstack([gride1,gride2])
NewGrid4=np.hstack([gride1,gride2])
# print(NewGrid3)
# print(NewGrid4)

a=np.array([1,2,3,99,99,3,2,1])
# print(np.split(a,4))
# print(np.split(a,[3,5]))

b=np.arange(16).reshape((4,4))
# print(b)

upper,lower=np.vsplit(b,[2])
# print(upper)
# print(lower)
left,right=np.hsplit(b,[2])
# print(left)
# print(right)




