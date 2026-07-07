import numpy as np
a = np.arange(15).reshape(3,5)

print(a)
print(f"a的每个维度的数组的大小{a.shape}")
print(f"a的轴数{a.ndim}")
print(f"a中每个元素的字节大小为{a.itemsize}")
print(f"a中数组元素的总数为{a.size}")
print(f"a的类型为{type(a)}")

b = np.array([1,2,3,4,5])
print(b)

c = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(c)

d = np.array([1,2,3,4,5], ndmin = 3)
print(d)

e = np.array([1,2,3,4,5,6], dtype = "float32")
print(e)