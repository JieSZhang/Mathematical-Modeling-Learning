import numpy as np

#ndarray.ndim用于返回数组的维数，等于秩
a = np.arange(24)
print(a.ndim)
b = a.reshape(2,4,3)
print(b.ndim)
print(b)

#ndarray.shape用于表示数组维度，返回一个元组，这个元组的长度就是维度的数目
#也可以用于调整数组大小
c = np.array([[1,2,3,4,5,6],[4,5,6,7,8,9]])
print(c.shape)
c.shape = (6,2)
print(c)
#还可以用NumPy中的reshape函数来调整数组大小
e = np.array([[1,2,3,4,5,6],[4,5,6,7,8,9]])
f = e.reshape(6,2)
print(f)

#ndarray.size是数组中元素的数量。等于np.prod(a.shape)，即数组尺寸的乘积。
# a.size返回一个标准的任意精度Python整数。
# 对于其他获得相同值的方法，情况可能并非如此（如建议的方法np.prod(a.shape)，该方法返回的一个实例np.int_），并且如果该值在可能溢出固定大小的整数类型的计算中进一步使用，则可能是相关的。#
x = np.zeros((3, 5, 2), dtype=np.complex128)
print(x)
print(x.size)
print(np.prod(x.shape))

#ndarray.dtype
y = np.array([[0, 1], [2, 3]])
print(y.dtype)
print(type(y.dtype))

#ndarray.itemsize以字节的形式返回数组中每一个元素的大小
x1 = np.array([1,2,3,4,5], dtype = np.int8)
print(x1.itemsize)
y1 = np.array([1,2,3,4,5], dtype = np.float64)
print(y1.itemsize)

#ndarray.flags 返回 ndarray 对象的内存信息，包含以下属性：
#1.C_CONTIGUOUS (C) - 数据是在一个单一的C风格的连续段中。
#2.F_CONTIGUOUS (F) - 数据是在一个单一的Fortran风格的连续段中。
#3.OWNDATA (O) - 数组拥有它所使用的内存或从另一个对象中借用它。
#4.WRITEABLE (W) - 数据区域可以被写入，将该值设置为 False，则数据为只读。
#5.ALIGNED (A) - 数据和所有元素都适当地对齐到硬件上。
#5.UPDATEIFCOPY (U) - 这个数组是其它数组的一个副本，当这个数组被释放时，原数组的内容将被更新。
g = np.array([1,2,3,4,5])
print(g.flags)

#nadarray.real和x.imag
h = np.sqrt([1+0j, 0+1j])
print(h.real)
print(h.real.dtype)
print(h.imag)
print(h.imag.dtype)