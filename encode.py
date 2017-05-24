#!/usr/bin/env python3
# -*- coding: utf-8 -*-


ord('A')
ord('中')
chr(25991)

print('\u4e2d\u6587')

# bytes 数据流，+b
x = b'ABC'

# encode
'ABC'.encode('ascii')
'中文'.encode('utf-8')


# decode
b'ABCd'.decode('ascii')
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
