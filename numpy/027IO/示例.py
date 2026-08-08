import numpy as np 
  
#numpy.save()
# a = np.array([1,2,3,4,5]) 
# # 保存到 test.npy 文件上
# np.save('test.npy',a) 
# # 保存到 test1.npy 文件上，如果文件路径末尾没有扩展名 .npy，该扩展名会被自动加上
# np.save('test1.npy',a)
# #我们可以使用 load() 函数来读取数据就可以正常显示
# b = np.load('test.npy') 
# print (b)

#np.savez
# a = np.array([[1,2,3],[4,5,6]])
# b = np.arange(0, 1.0, 0.1)
# c = np.sin(b)
# # c 使用了关键字参数 sin_array
# np.savez("nhooo.npz", a, b, sin_array = c)
# r = np.load("nhooo.npz") 
# print(r.files) # 查看各个数组名称
# print(r["arr_0"]) # 数组 a
# print(r["arr_1"]) # 数组 b
# print(r["sin_array"]) # 数组 c

#savetxt()
# a = np.array([1,2,3,4,5]) 
# np.savetxt('out.txt',a) 
# b = np.loadtxt('out.txt')   
# print(b)
#使用 delimiter 参数
a=np.arange(0,10,0.5).reshape(4,-1)
np.savetxt("out.txt",a,fmt="%d",delimiter=",") # 改为保存为整数，以逗号分隔
b = np.loadtxt("out.txt",delimiter=",") # load 时也要指定为逗号分隔
print(b)