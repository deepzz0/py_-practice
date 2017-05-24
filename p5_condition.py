#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# 条件判断
a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# if elif else
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')


# True
# 只要x是非零数值、非空字符串、非空list等，就判断为True
x = 1
if x:
    print('True')


# 再议 input
s = input('birth: ')
birth = int(s) # 输入的是字符串，转为 int
if birth < 2000:
    print('00前')
else:
    print('00后')
