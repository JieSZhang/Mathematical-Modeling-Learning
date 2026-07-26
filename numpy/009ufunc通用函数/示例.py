import time
import math 
import numpy as np

# ##math与numpy函数的性能比较
# x = [i * 0.001 for i in np.arange(1000000)]
# start1 = time.perf_counter()
# for i, t in enumerate(x):
#     x[i] = math.sin(t)
# print("math.sin:", time.perf_counter() - start1)
# y = x.copy()
# y = np.array(y)
# start2 = time.perf_counter()
# np.sin(x)
# print ("numpy.sin:", time.perf_counter() - start2 )

# #向量化
# """
# 将迭代语句转换为基于向量的操作称为向量化。
# 由于现代 CPU 已针对此类操作进行了优化，因此速度更快。
# 对两个列表的元素进行相加：
# list 1: [1, 2, 3, 4]
# list 2: [4, 5, 6, 7]
# 一种方法是遍历两个列表，然后对每个元素求和。
# 如果没有 ufunc，我们可以使用 Python 的内置 zip() 方法：
# """
# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = []
# for i, j in zip(x, y):
#     z.append(i + j)
# print(z)
# #对此，NumPy 有一个 ufunc，名为 add(x, y)，它会输出相同的结果，通过 ufunc，我们可以使用 add() 函数：
# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# z = np.add(x,y)
# print(z)

"""
循环与向量运算比较
充分使用 Python 的 NumPy 库中的内建函数（Built-in Function），来实现计算的向量化，可大大地提高运行速度。
NumPy 库中的内建函数使用了 SIMD 指令。如下使用的向量化要比使用循环计算速度快得多。
如果使用 GPU，其性能将更强大，不过 Numpy 不支持 GPU。
"""
x1 = np.random.rand(1000000)
x2 = np.random.rand(1000000)
##使用循环计算向量点积
tic = time.process_time()
dot = 0
for i in range(len(x1)):
    dot+= x1[i]*x2[i]
toc = time.process_time()
print ("dot = " + str(dot) + "\n for循环-----计算时间 = " + str(1000*(toc - tic)) + "ms")
##使用numpy函数求点积
tic = time.process_time()
dot = 0
dot = np.dot(x1,x2)
toc = time.process_time()
print ("dot = " + str(dot) + "\n Verctor 版本---- 计算时间 = " + str(1000*(toc - tic)) + "ms")