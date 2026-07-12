import numpy as np

# #numpy.empty
# print(np.empty([2,2]))
# print(np.empty([2,2], dtype=int))

# #numpy.empty_like
# a = np.array([[1,2,3], [4,5,6]])
# print(np.empty_like(a))
# b = np.array([[1., 2., 3.], [4., 5., 6.]])
# print(np.empty_like(b))

# #numpy.zeros
# print(np.zeros(5))
# print(np.zeros((5,), dtype=int))
# print(np.zeros((2, 1)))
# s = (2, 2)
# print(np.zeros(s, dtype=[('x', 'i4'),('y','i4')]))

# #numpy.zeros_like
# x = np.arange(6)
# x = x.reshape((2, 3))
# print(x)
# print(np.zeros_like(x))
# y = np.arange(3, dtype=float)
# print(y)
# print(np.zeros_like(y))

# #numpy.ones
# print(np.ones(5))
# print(np.ones((5,), dtype=int))
# print(np.ones((2, 1)))
# s = (2, 2)
# print(np.ones(s, dtype=[('x', 'i4'),('y', 'i4')]))

# #numpy.ones_like
# x = np.arange(6)
# x = x.reshape((2, 3))
# print(x)
# print(np.ones_like(x))
# y = np.arange(3, dtype=float)
# print(y)
# print(np.ones_like(y))

# #numpy.arange
# print(np.arange(3))
# print(np.arange(3.0))
# print(np.arange(3,7))
# print(np.arange(3,7,2))

# #numpy.linspace
# a = np.linspace(1,10,10)
# print(a)
# b = np.linspace(10, 20, 5, endpoint=False)
# print(b)
# c = np.linspace(1,10,10,retstep=True)
# print(c)
# d = np.linspace(1,10,10).reshape([10,1])
# print(d)

# #numpy.asarray
# #直接对列表进行转换
# ls1 = [10, 42, 0, -17, 30]
# nd1 = np.array(ls1)
# print(nd1)
# print(type(nd1))
# #使用numpy.asarray
# x = [1, 2, 3]
# a = np.asarray(x)
# print(a)
# y = [(1,2,3),(4,5,6)]
# b = np.asarray(y)
# print(b)
# z = [1,2,3]
# c = np.asarray(z, dtype=float)
# print(c)

# #numpy.frombuffer
# s = b'Hello World'
# a = np.frombuffer(s, dtype='S1')
# print(a)

# #numpy.fromiter
# list = range(5)
# it = iter(list)
# print(it)
# x = np.fromiter(it, dtype=float)
# print(x)

#生成矩阵
#生成全是0的3×3矩阵
nd5 = np.zeros([3,3])
print("nd5=\n", nd5)
#生成全是1的3×3矩阵
nd6 = np.ones([3,3])
print("nd6=\n", nd6)
#生成4阶的单位矩阵
nd7 = np.eye(4)
print("nd=\n",nd7)
#生成4阶对角矩阵
nd8 = np.diag([1, 8, 3, 10])
print("nd=\n", nd8)