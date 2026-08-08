import numpy as np

#numpy.char.add()
# print ('连接两个字符串：',np.char.add(['hello'],[' nhooo']))
# print ('\n')
# print ('连接示例：',np.char.add(['hello', 'hi'],[' numpy', ' nhooo']))

#numpy.char.multiply()
# print (np.char.multiply('wow,nhooo！ ',5))

#numpy.char.center()
# np.char.center(str, width,fillchar) ：
# str: 字符串，width: 长度，fillchar: 填充字符
# print (np.char.center('Nhooo', 30,fillchar = '.'))

#numpy.char.capitalize()
# print (np.char.capitalize('nhooo'))

#numpy.char.title()
# print (np.char.title('hello nhooo, i like you.'))

#numpy.char.lower()
# #操作数组
# print (np.char.lower(['LIDIHUO','WEBSITE']))
# #操作字符串
# print (np.char.lower('LIDIHUO'))

#numpy.char.upper()
# #操作数组
# print (np.char.upper(['nhooo','website']))
# # 操作字符串
# print (np.char.upper('nhooo'))

#numpy.char.split()
# # 分隔符默认为空格
# print (np.char.split('hello nhooo i like you'))
# # 分隔符为 .
# print (np.char.split('www.cainiaojc.com', sep = '.'))

#numpy.char.splitlines()
# print(np.char.splitlines('i\nlike nhooo')) 
# print(np.char.splitlines('i\rlike nhooo'))

#numpy.char.strip()
# # 移除字符串头尾的 a 字符
# print (np.char.strip('aaaa abbb acccc','a'))
# # 移除数组元素头尾的 a 字符
# print (np.char.strip(['aaaa','abbb','cccca'],'a'))

#numpy.char.join()
# # 操作字符串
# print (np.char.join(':','nhooo'))
# # 指定多个分隔符操作数组元素
# print (np.char.join([':','-'],['nhooo','google']))

#numpy.char.replace()
# print (np.char.replace ('i like nhooo', 'nh', 'aa'))

#numpy.char.encode()
# a = np.char.encode('nhooo', 'cp500') 
# print (a)

#numpy.char.decode()
# a = np.char.encode('nhooo', 'cp500') 
# print (a)
# print (np.char.decode(a,'cp500'))