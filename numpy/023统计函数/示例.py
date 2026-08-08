import numpy as np 

#numpy.amin() 和 numpy.amax()
# a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 
# print ('我们的数组是：',a)
# print ('调用 amin() 函数：',np.amin(a,1))
# print ('再次调用 amin() 函数：',np.amin(a,0))
# print ('调用 amax() 函数：',np.amax(a))
# print ('再次调用 amax() 函数：',np.amax(a, axis = 0))

#numpy.ptp()
# a = np.array([[3,7,5],[8,4,3],[2,4,9]]) 
# print ('调用 ptp() 函数：',np.ptp(a))
# print ('沿轴 1 调用 ptp() 函数：',np.ptp(a, axis = 1))
# print ('沿轴 0 调用 ptp() 函数：',np.ptp(a, axis = 0))

#numpy.percentile()
# a = np.array([[10, 7, 4], [3, 2, 1]])
# # 50% 的分位数，就是 a 里排序之后的中位数
# print ('调用 percentile() 函数：',np.percentile(a, 50)) 
# # axis 为 0，在纵列上求
# print (np.percentile(a, 50, axis=0)) 
# # axis 为 1，在横行上求
# print (np.percentile(a, 50, axis=1)) 
# # 保持维度不变
# print (np.percentile(a, 50, axis=1, keepdims=True))

#numpy.median()
# a = np.array([[30,65,70],[80,95,10],[50,90,60]]) 
# print ('调用 median() 函数：',np.median(a))
# print ('沿轴 0 调用 median() 函数：',np.median(a, axis = 0))
# print ('沿轴 1 调用 median() 函数：',np.median(a, axis = 1))

#numpy.mean()
# a = np.array([[1,2,3],[3,4,5],[4,5,6]]) 
# print ('调用 mean() 函数：',(np.mean(a)))
# print ('沿轴 0 调用 mean() 函数：',np.mean(a, axis = 0))
# print ('沿轴 1 调用 mean() 函数：',np.mean(a, axis = 1))

#numpy.average()
# a = np.array([1,2,3,4]) 
# print ('调用 average() 函数：',np.average(a))
# # 不指定权重时相当于 mean 函数
# wts = np.array([4,3,2,1]) 
# print ('再次调用 average() 函数：',np.average(a,weights = wts))
# # 如果 returned 参数设为 True，则返回权重的和 
# print ('权重的和：',np.average([1,2,3, 4],weights = [4,3,2,1], returned =  True))
#在多维数组中，可以指定用于计算的轴。
# a = np.arange(6).reshape(3,2) 
# wt = np.array([3,5]) 
# print ('修改后的数组：',np.average(a, axis = 1, weights = wt))
# print ('修改后的数组：',np.average(a, axis = 1, weights = wt, returned =  True))

#标准差
# print (np.std([1,2,3,4]))

#方差
# print (np.var([1,2,3,4]))