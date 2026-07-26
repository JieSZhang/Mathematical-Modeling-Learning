##NumPy生成的多维数组对象ndarray，是一系列同类型数据的集合，以0为下标开始，与python原有的数组对象array相比拥有更多功能，更重要的属性

##ndarray内部由以下内容组成
1.一个指向数据（内存或内存映射文件中的一块数据）的指针
2.数据类型或dtype，描述在数组中的固定大小值的格子
3.一个表示数组形状的元组，表示各维度大小的元组
4.一个跨度元组，其中的整数指的是为了前进到当前维度下一个元素需要“跨过”的字节数

##ndarray对象重要属性
（1）ndarray.ndim-数组的轴（维度）的个数。在python世界中，维度的数量被称为rank。
（2）ndarray.shape-数组的维度。这是一个整数的元组，表示每个维度中数组的大小。shape元组的长度就是rank或维度的个个数ndim。
（3）ndarray.size-数组元素的总数。这等于shape的元素的乘积。
（4）ndarraay.dtype-一个描述数组中元素类型的对象。可以使用标准的Python类型创建或指定dtype。另外Numpy提供它自己的类型。
（5）ndarray.itemsize-数组中每个元素的字节大小。
（6）ndarray.data-该缓冲区包含数组的实际元素。通常，我们不需要使用此属性，因为我们将使用索引访问数组中的元素。

##numpy.array函数的参数说明
numpy.array（object, dtype = None, copy = True, order = None, subok = False, ndmin = 0）
1.object-数组或嵌套的数列
2.dtype-数组元素的数据类型，可选
3.copy-对象是否需要复制
4.order-创建数组的样式，C为行方向，F为列方向，A为任意方向（默认）
5.subok-默认返回一个与基类类型一致的数组
6.ndmin-指定生成数组的最小维度