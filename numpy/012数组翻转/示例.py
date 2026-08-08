import numpy as np
 
# #numpy.transpose
# a = np.arange(12).reshape(3,4)
# print ('原数组：')
# print (a)
# print ('\n')
# print ('对换数组：')
# print (np.transpose(a))

# #numpy.ndarray.T
# a = np.arange(12).reshape(3,4)
# print ('原数组：')
# print (a)
# print ('\n')
# print ('转置数组：')
# print (a.T)

# #numpy.rollaxis
# # 创建了三维的 ndarray
# a = np.arange(8).reshape(2,2,2)
# print ('原数组：')
# print (a)
# print ('\n')
# # 将轴 2 滚动到轴 0（宽度到深度）
# print ('调用 rollaxis 函数：')
# print (np.rollaxis(a,2))
# # 将轴 0 滚动到轴 1：（宽度到高度）
# print ('\n')
# print ('调用 rollaxis 函数：')
# print (np.rollaxis(a,2,1))

# #numpy.swapaxes
# # 创建了三维的 ndarray
# a = np.arange(8).reshape(2,2,2)
# print ('原数组：')
# print (a)
# print ('\n')
# # 现在交换轴 0（深度方向）到轴 2（宽度方向）
# print ('调用 swapaxes 函数后的数组：')
# print (np.swapaxes(a, 2, 0))