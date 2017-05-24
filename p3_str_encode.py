#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 理解 ASICC 与 UNICODE 的关系
# 什么又是 UTF-8？

print('\u4e2d\u6587')

# 转为 bytes 数据流，+b
x = b'ABC'
# 字符转换
print(ord('A')) # 65
print(ord('中')) # 20013
print(chr(25991)) # ‘文’

# encode 编码
'ABC'.encode('ascii')
'中文'.encode('utf-8')

# decode 解码
b'ABCd'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 长度
print(len('ABC')) # 3
print(len('中文')) # 2
print(len(b'ABC')) # 3
print(len('中文'.encode('utf-8'))) # 6
print(len(b'\xe4\xb8\xad\xe6\x96\x87')) # 6

