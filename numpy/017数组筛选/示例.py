import numpy as np

# #数组过滤
# arr = np.array([61, 62, 63, 64, 65])
# x = [True, False, True, False, True]
# newarr = arr[x]
# print(newarr)

#创建过滤数组
# #创建一个仅返回62的值的过滤器数组
# arr = np.array([61, 62, 63, 64, 65])
# #创建一个空列表
# filter_arr = []
# #遍历arr中的每个元素
# for element in arr:
#     #如果元素大于62，则将值设置为True，否则为False：
#     if element > 62:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)
# #创建一个过滤数组，该数组仅返回原始数组中的偶数元素
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# #创建一个空列表
# filter_arr = []
# #遍历arr中的每个元素
# for element in arr:
#     #如果元素可以被2整除，则将值设置为True，否则设置为False
#     if element % 2 == 0:
#         filter_arr.append(True)
#     else:
#         filter_arr.append(False)
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)

#直接从数组创建过滤器
# #创建一个仅返回大于62的值的过滤器数组
# arr = np.array([61, 62, 63, 64, 65])
# filter_arr = arr > 62
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)
# #创建一个过滤器数组，该数组仅返回原始数组的偶数元素
# arr = np.array([1, 2, 3, 4, 5, 6, 7])
# filter_arr = arr % 2 == 0
# newarr = arr[filter_arr]
# print(filter_arr)
# print(newarr)