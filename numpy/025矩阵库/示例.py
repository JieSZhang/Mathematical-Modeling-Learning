import numpy.matlib 
import numpy as np

#matlib.empty()
# print (np.matlib.empty((3,3)))

#numpy.matlib.zeros()
# print (np.matlib.zeros((3,3)))

#numpy.matlib.ones()
# print (np.matlib.ones((3,3)))

#numpy.matlib.eye()
# print (np.matlib.eye(n = 3, M = 4, k = 0, dtype = float))

#numpy.matlib.identity()
#print (np.matlib.identity(5, dtype = float))

#numpy.matlib.rand()
print (np.matlib.rand(3,3))

#矩阵总是二维的，而 ndarray 是一个 n 维数组。 两个对象都是可互换的。
# i = np.matrix('1,2;3,4') 
# print (i)
# j = np.asarray(i) 
# print (j)
# k = np.asmatrix (j) 
# print (k)