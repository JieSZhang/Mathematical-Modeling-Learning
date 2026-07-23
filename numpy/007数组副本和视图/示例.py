import numpy as np

# #引用（无复制）
# a = np.arange(6)
# print(a)
# print(id(a))
# b = a
# print(b)
# print(id(b))
# b.shape = 3,2
# print(b)
# print(a)

#视图或浅拷贝
# a = np.arange(6).reshape(3,2)
# print(a)
# b = a.view()
# print(b)
# print(id(a))
# print(id(b))
# #修改b的形状，并不会修改a
# b.shape = 2,3
# print(b)
# print(a)
#使用切片创建视图修改数据会影响到原始数组
# arr = np.arange(12)
# print(arr)
# a=arr[2:]
# b=arr[2:]
# a[1] = 123456
# b[2] = 23445
# print(arr)
# print(id(a),id(b),id(arr[3:]))

#副本或深拷贝
a = np.array([[10,10],[2,3],[4,5]])
print(a)
b = a.copy()
print(b)
b[0,0] = 100
print(b)
print(a)