import numpy as np
big_arry=np.random.randint(1,1e2,100000)# 参数12 大小区间，参数3 随机数个数
# print(1/big_arry)#统一取倒

# print(np.arange(5)/np.arange(1,6))
# print(2*np.arange(5))
x=np.arange(9).reshape((3,3))
# print(x)
# print(2**x)#以2为底的指数幂
# print(x**x)
# print(x//3)#整除取商
# print(x%3)#整除取余
# print(1/x)
# print(np.log1p(x))
# print(np.log2(x))
# print(np.log10(x))
y=np.arange(1,6)
# print(y)
# print (np.add.reduce(y))#加
# print (np.multiply.reduce(y))#乘
# print (np.add.accumulate(y))# ∑
# print (np.multiply.accumulate(y))#阶乘

big_arry2=np.random.random(10000000)
# print(np.min(big_arry2),np.max(big_arry2))
test=np.random.randint(10,size=(10,10))#参数1省略默认0  生成一个0-10的10*10的矩阵
# print(test)
# print(test.min(axis=0))#最小的columns


a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
# print(a + b)
M = np.ones((3, 3))
# print(M)
# print(M + a)

a = np.arange(3)
b = np.arange(3)[:, np.newaxis]
# print(a)
# print(b)
# print(a + b)#!!!!???
# print(np.repeat([a],3,axis=0))
# print(np.repeat(b,3,axis=1))
# print(np.repeat(b,3,axis=1)+np.repeat([a],3,axis=0),a + b)


# M = np.ones((3, 2))
# a = np.arange(3)
# print(M)
# print(a)
# print(M + a)#erro

# a = np.array([4,5,6,7])  
# b = np.array([1,3,5,7,9,11,14,10])  
# c = a + b;  #erro

matrix1 = np.array([[1, 3], [5, 7]])
             
matrix2 = np.array([[2, 6], [4, 8]])

result = np.dot(matrix1, matrix2)

print("matrix1 x matrix2: \n",result)#?????!!!!!


matrix1 = np.random.randint(10,size=(3,2))
print(matrix1)
matrix2 = np.random.randint(10,size=(2,3))
print(matrix2)
print("\n")
print(np.dot(matrix1,matrix2))
print("\n")
print(np.dot(matrix2,matrix1))
# print(np.dot(matrix1,matrix1))#erro

matrix1=np.array([1,2,3])
matrix2 = np.random.randint(10,size=(3,3))
print("\n")
print(np.dot(matrix2,matrix1))
print("\n")
print(np.matmul(matrix2,matrix1))
print("\n")
print(matrix1)
print(np.multiply(matrix1,matrix1),"\n")



matrix1 = np.array([[1, 3], [5, 7]])
print(matrix1 ,"\n")
print(matrix1 - matrix1 ,"\n")
# matrix1 = matrix1 + matrix1
# print(matrix1 ,"\n")
np.add(matrix1,matrix1,out=matrix1)
print(matrix1 ,"\n")
print(matrix1.T ,"转置矩阵 \n")
print(np.linalg.det(matrix1) ,"\n")
print(np.linalg.inv(matrix1) ,"\n")
print(np.dot(matrix1, np.linalg.inv(matrix1)).astype(int) ,"\n")


print(x,"1 \n")
x[x>2]=0 #对矩阵中大于2的全部变成0
print(x ,"2 \n")
print(np.any(x==0) ,"\n")
print(np.all(x==0) ,"\n")
print(np.sum(x>1) ,"\n")#个数
print(np.sum(x[x>1]) ,"\n")#值


print(matrix1,"\n")
print(np.where(matrix1 == 14),"\n")


Z = np.random.randint(1,10, 10)
print(Z,"\n")
print(Z.argmin(),"\n")

Z[Z.argmax()] = 0
print(Z,"\n")
print(Z.argmin(),"\n")

