#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 整数
a = 1
a = a + 2
b = 0xff00
print(a, b)

# 浮点数
c = 1.23
c = -9.01
c = 1.2e-10
print(c)

# 字符串
d = 'test1'
d = "test2"
d = 'i\'m test3'
d = '''line1
line2
'''
print(d)

c = 'test' # 解释器创建了字符串 test 和变量 c，并把 c 指向了字符串 test
d = c # 解释器创建了变脸 d，并把 d 指向了字符串 test
c = 'test2' # 解释器穿件了字符串 test2，把 c 指向了字符串 test2
print(d) # test


# 布尔值
b = True
b = False
b = 3 > 5
b = True & True
b = True or False
b = not True
b = not False
b = 5 > 3 or 1 > 3
print(b)

# 空值
e = None
print(e)

# 常量，通常全大写
PI = 3.141592654

# 结果均为浮点
print(10 / 3) # 3.333333
print(9 / 3) # 3.0

# 整除
print(10 // 3) # 3

# 取余
print(10 % 3) # 1
