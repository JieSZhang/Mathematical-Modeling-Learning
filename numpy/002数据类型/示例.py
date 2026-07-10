import numpy as np

a = np.dtype('i8')
print(a)

b = np.dtype([('number',np.int16)])
print(b)
arr = np.array([(1,),(2,),(3,)], dtype=b)
print(arr)
print(arr['number'])

 #定义某个结构体的数据类型并进行命名
animal = np.dtype([('name','S20'),('age','i1'),('marks','f4')])
print(animal)
c = np.array([('cat', 5, 10),('dog', 4, 35),('lion', 8, 18)], dtype = animal)
print(c)
 
#可以使用arr.astype()方法修改类型
arr1 = np.array([1,2,3,4,5])
print(arr1.dtype)
float_arr1 = arr1.astype('float32')
print(float_arr1.dtype)
print(float_arr1)
#注意，如果数组元素是整数可以转换为浮点数，但是浮点数不能强制转化为整数

#可以使用其他数组的类型属性作为参数进行类型转换
int_arr = np.arange(10)
calibers = np.array([.22, .270, .357], dtype=np.float64)
print(calibers)
arr_last = int_arr.astype(calibers.dtype)
print(arr_last.dtype)
print(arr_last)