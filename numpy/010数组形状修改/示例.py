import numpy as np

# #打印2-D数组的形状
# arr = np.array([[1, 2, 3, 4],[5, 6, 7, 8]])
# print(arr.shape)
#利用ndmin创建一个只有四个数的五维数组
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print("shape of array: ", arr.shape)

#修改数组形状
# #将1-D重塑为2-D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(4, 3)
# print(newarr)
# #将1-D重塑为3-D
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# newarr = arr.reshape(2, 3, 2)
# print(newarr)
# #错误示范
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3, 3)
# print(newarr)

# #未知的维
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(2,2,-1)
# print(newarr)

# #展平数组
# arr = np.array([[1, 2, 3],[4, 5, 6]])
# newarr = arr.reshape(-1)
# print(newarr)