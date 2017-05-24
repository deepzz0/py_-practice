#!/usr/bin/env python3
# -*- coding: utf-8 -*-

a = 'Hello, %s' % 'world'
print(a)

b = 'Hi, %s, you have $%d.' % ('Michael', 10000)
print(b)

# 占位
c = '%2d-%02d' % (3, 1)
print(c)
d = '%.2f' % 3.1415926
print(d)

# 不确定用 %?，可使用 %s
e = 'Age: %s, Gender: %s' % (25, True)
print(e)

# 普通字符 %
f = 'growth rate: %d %%' % 7
print(f)
