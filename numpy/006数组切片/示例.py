import numpy as np

# #数组切片
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1: 5])
# print(arr[4:])
# print(arr[:4])

# #负裁切
# #从末尾开始的索引3到末尾开始的索引1，对数组进行裁切
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[-3:-1])

# #STEP步长
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# print(arr[1:5:2])
# print(arr[::2])

# #裁切2-D数组
# arr = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
# print(arr[1, 1:4])
# print(arr[0:2, 2])
# print(arr[0:2, 1:4])

# 整数数组索引
# #以下实例获取数组中(0,0)，(1,1)，(2,0)位置处的元素
# x = np.array([[1, 2], [3, 4], [5, 6]])
# y = x[[0,1,2],[0,1,0]]
# print(y)
# #以下实例获取了4×3数组中的四个角的元素。行索引是[0,0]和[3,3]，而列索引是[0,2]和[0,2]
# x = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8],[9, 10, 11]])
# print(x)
# rows = np.array([[0,0],[3,3]])
# cols = np.array([[0,2],[0,2]])
# y = x[rows,cols]
# print(y)
# #可以建筑切片或...与索引数组组合
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# b = a[1:3, 1:3]
# c = a[1:3, [1,2]]
# d = a[...,1:]
# print(b)
# print(c)
# print(d)

#布尔索引
# #以下实例获取大于5的元素
# x = np.array([[0, 1, 2],[3, 4, 5],[6, 7, 8],[9, 10, 11]])
# print(x)
# print(x[x>5])
# #以下示例使用~（取补运算符）来过滤NaN
# a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
# print(a[~np.isnan(a)])
# #以下实例演示如何从数组中过滤掉非复数元素
# a = np.array([1, 2+6j, 5, 3.5+5j])
# print(a[np.iscomplex(a)])

##花式索引
x = np.arange(32).reshape(8,4)
print(x[[4,2,1,7]])
print(x[[-4,-2,-1,-7]])
print(x[np.ix_([1,5,7,2],[0,3,1,2])])