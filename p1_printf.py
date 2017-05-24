#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 普通打印
print('hahaha')

# 多行打印
print('''line1
line2
line3''')

# 转义字符
print('line1\nline2')
print('hello i\'m jack')

# 打印数值
print(1.23e10)
print(0x11)
print(1>2)
print(2>1)
print(100 + 200)

# 打印布尔值
print(False)
print(True and True)
print(True or False)
print(None)

# 中文其它语言
print('这里是中国')

# 字符串格式化
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))

# 常见占位符
# %d	整数
# %f	浮点数
# %s	字符串
# %x	十六进制整数
print('%2d-%02d' % (3, 1))
print('Age: %s. Gender: %s' % (25, True)) # %s 永远起作用，当你不知道用什么的时候
print('growth rate: %d %%' % 7) # 转义 %

# 占位
c = '%2d-%02d' % (3, 1)
print(c)
d = '%.2f' % 3.1415926
print(d)
