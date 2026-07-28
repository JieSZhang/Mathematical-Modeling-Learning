import numpy as np

#NumPy位运算
# a = np.array([1, 2, 3])
# b = np.array([2, 2, 2])
# print(a * b)
#形状不同时，自动触发广播机制
# a = np.array([[ 0, 0, 0],
#             [10,10,10],
#             [20,20,20],
#             [30,30,30]])
# b = np.array([1,2,3])
# print(a + b)
#上述代码等效于将b在二维上重复四次
# a = np.array([[ 0, 0, 0],
#             [10,10,10],
#             [20,20,20],
#             [30,30,30]])
# b = np.array([1,2,3])
# bb = np.tile(b, (4, 1))
# print(a + bb)

# #一般广播规则
# x = np.arange(4)
# xx = x.reshape(4,1)
# y = np.ones(5)
# z = np.ones((3,4))
# print(x.shape)
# print(y.shape)
# #print(x + y)    #错误示例
# print(xx.shape)
# print(y.shape)
# print((xx + y).shape)
# print(xx + y)
# print(x.shape)
# print(z.shape)
# print((x + z).shape)
# print(x + z)
# #广播提供了一种方便的方式来获取两个数组的外积
# a = np.array([0.0, 10.0, 20.0, 30.0])
# b = np.array([1.0, 2.0, 3.0])
# print(a[:, np.newaxis] + b) 
# #newaxis的作用是为a添加了一个新的轴