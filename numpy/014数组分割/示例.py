import numpy as np

# #numpy.split
# a = np.arange(15)
# print ('第一个数组：')
# print (a)
# print ('\n')
# print ('将数组分为三个大小相等的子数组：')
# b = np.split(a,5)
# print (b)
# print ('\n')
# print ('将数组在一维数组中表明的位置分割：')
# b = np.split(a,[4,7])
# print (b)
# #当数组中的元素少于要求的数量，需要用array_split函数它将从末尾进行相应调整。
# arr = np.array([1, 2, 3, 4, 5, 6])
# newarr = np.array_split(arr, 4)
# print(newarr)

# #numpy.hsplit
# harr = np.floor(10 * np.random.random((2, 8)))
# print("原始array：")
# print(harr)
# print("拆分后：")
# print(np.hsplit(harr, 4))

# #numpy.vsplit
# a = np.arange(16).reshape(4,4)
# print ('第一个数组：')
# print (a)
# print ('\n')
# print ('竖直分割：')
# b = np.vsplit(a,2)
# print (b)