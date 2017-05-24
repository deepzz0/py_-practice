#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# 数值
a = 1
a = a + 2
print(a)

# 布尔值
b = True
b = False
print(b)

# 字符串
c = 'test' # 解释器创建了字符串 test 和变量 c，并把 c 指向了字符串 test
d = c # 解释器创建了变脸 d，并把 d 指向了字符串 test
c = 'test2' # 解释器穿件了字符串 test2，把 c 指向了字符串 test2
print(d)

e = '中文'
print(len(c)) # 5
print(len(e)) # 2
print(len(e.encode('utf-8'))) # 6

# 常量，通常全大写
PI = 3.141592654
