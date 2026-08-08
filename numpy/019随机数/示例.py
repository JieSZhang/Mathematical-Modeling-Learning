from numpy import random

#生成随机数
# x = random.randint(100)
# print(x)

#生成随机浮点数
# x = random.rand()
# print(x)

#生成随机数组
# #以下演示生成一个 1-D 数组，其中包含 5 个从 0 到 100 之间的随机整数
# x = random.randint(100, size=(5))
# print(x)
# #生成有 3 行的 2-D 数组，每行包含 5 个从 0 到 100 之间的随机整数
# x = random.randint(100, size=(3, 5))
# print(x)
# #以下演示生成包含 5 个随机浮点数的 1-D 数组
# x = random.rand(5)
# print(x)
# #生成有 3 行的 2-D 数组，每行包含 5 个随机数
# x = random.rand(3, 5)
# print(x)

#choice()从数组生成随机数
# #生成一个值
# x = random.choice([3, 5, 7, 9])
# print(x)
# #生成一个二维数组
# x = random.choice([3, 5, 7, 9], size=(3, 5))
# print(x)