import numpy as np

# #数组迭代
# #创建一个2×6的数组，并使用nditer对它进行迭代
# a = np.arange(12).reshape(2,6)
# print("原始数组是：")
# print(a)
# print("\n")
# print("迭代输出元素：")
# for x in np.nditer(a):
#     print(x, end=" ")  #默认为行优先
# #a.T为数组a的转置数组，如果是二维数组就等同于矩阵的转置
# #np.nditer()方法按照内存中存储的顺序遍历
# for x in np.nditer(a.T):
#     print(x, end=" ")  #由此可知，转置数组和原数组在内存中存储顺序一样
# print("\n")
# for x in np.nditer(a.T.copy(order="C")):
#     print(x, end=" ") #由此可知，copy出的数组存储顺序不同

# #控制遍历顺序
# a = np.arange(0,100,5)
# a = a.reshape(4,5)
# print("原始数组是：")
# print(a)
# print("\n")
# print("原始数组的转置是：")
# b = a.T
# print(b)
# print("\n")
# #创造一个副本，并对内存顺序有实质修改
# print("以C风格顺序排序：")
# c = b.copy(order="C")
# print(c)
# for x in np.nditer(c):
#     print(x, end=" ")
# print("\n")
# print("以F风格顺序排序：")
# d = b.copy(order="F")
# print(d)
# for x in np.nditer(d):
#     print(x, end=" ")
# #对内存顺序没有修改，只是在排列时指定顺序
# print("\n")
# print("以C风格顺序排序：")
# for x in np.nditer(a, order="C"):
#     print(x, end=", ")
# print("\n")
# print("以F风格顺序排序：")
# for x in np.nditer(a, order="F"):
#     print(x, end=", ")

# #修改数组中元素的值
# a = np.arange(0,100,5)
# a = a.reshape(4,5)
# print("原始数组是：")
# print(a)
# print("\n")
# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...]=2*x
# print("修改后的数组是：")
# print(a)

# #使用外部循环
# a = np.arange(0,100,5)
# a = a.reshape(4,5)
# print("原始数组是：")
# print(a)
# print("\n")
# print("修改后的数组是：")
# for x in np.nditer(a, flags = ['external_loop'], order='F'):
#     print(x, end=" ")

#广播迭代
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('第一个数组为：')
print (a)
print ('\n')
print ('第二个数组为：')
b = np.array([1, 2, 3, 4], dtype = int)
print (b)
print ('\n')
print ('修改后的数组为：')
for x,y in np.nditer([a,b]):
    print ("%d:%d" % (x,y), end=" " )