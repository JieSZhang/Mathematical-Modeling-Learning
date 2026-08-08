import numpy.matlib
import numpy as np

#numpy.dot()
# a = np.array([[1,2],[3,4]])
# b = np.array([[11,12],[13,14]])
# print(np.dot(a,b))

#numpy.vdot()
# a = np.array([[1,2],[3,4]]) 
# b = np.array([[11,12],[13,14]])   
# # vdot 将数组展开计算内积
# print (np.vdot(a,b))

#numpy.inner()
# print (np.inner(np.array([1,2,3]),np.array([0,1,0])))
# # 等价于 1*0+2*1+3*0
# #二维情况
# a = np.array([[1,2], [3,4]])   
# print ('数组 a：')
# print (a)
# b = np.array([[11, 12], [13, 14]])   
# print ('数组 b：')
# print (b)  
# print ('内积：')
# print (np.inner(a,b))

#numpy.matmul
#对于二维数组,就是矩阵乘法
# a = [[1,0],[0,1]] 
# b = [[4,1],[2,2]] 
# print (np.matmul(a,b))
#二维和一维运算
# a = [[1,0],[0,1]] 
# b = [1,2] 
# print (np.matmul(a,b))
# print (np.matmul(b,a))
#维度大于二的数组
# a = np.arange(8).reshape(2,2,2) 
# b = np.arange(4).reshape(2,2) 
# print (np.matmul(a,b))

#numpy.linalg.det()
#二阶
# a = np.array([[1,2], [3,4]]) 
# print (np.linalg.det(a))
#三阶
# b = np.array([[6,1,1], [4, -2, 5], [2,8,7]]) 
# print (b)
# print (np.linalg.det(b))
# print (6*(-2*7 - 5*8) - 1*(4*7 - 5*2) + 1*(4*8 - -2*2))

#numpy.linalg.inv()
# x = np.array([[1,2],[3,4]]) 
# y = np.linalg.inv(x) 
# print (x)
# print (y)
# print (np.dot(x,y))
#现在创建一个矩阵A的逆矩阵
# a = np.array([[1,1,1],[0,2,5],[2,5,-1]])   
# print ('数组 a：')
# print (a)
# ainv = np.linalg.inv(a)  
# print ('a 的逆：')
# print (ainv)  
# print ('矩阵 b：')
# b = np.array([[6],[-4],[27]]) 
# print (b) 
# print ('计算：A^(-1)B：')
# x = np.linalg.solve(a,b) 
# print (x)
# # 这就是线性方向 x = 5, y = 3, z = -2 的解