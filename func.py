#!/usr/bin/env python3
# -*- coding: utf-8 -*-


print(abs(-1))
print(max(1, 2, 3, 4, 5))

print(int('123'))
print(int(123.34))
print(float('123.34'))
print(str(1.23))
print(bool(1))
print(bool(''))

# 将变量指向函数，也可以调用
a = abs
print(a(-1))




# 自定义函数
def my_abs(x):
    """取绝对值

    :x: TODO
    :returns: TODO

    """
    if x >=0:
        return x
    else:
        return -x

print(my_abs(-9))
print(my_abs(9))

# 如果想定义什么也不做的空函数
# 可以用 pass
def nop(arg1):
    """TODO: Docstring for nop.

    :arg1: TODO
    :returns: TODO

    """
    pass


# 参数检查
# 如果参数个数不对，python 解释器会自动检查出
# 并且抛出 TypeError 错误。
# 如：my_abs(1, 2)
#
# 但是如果参数类型不对，解释器就无法帮我们检查
# 如：my_abs('A')
#
# 完善 my_abs
def my_abs2(x):
    """完善的 my_abs

    :x: 整数
    :returns: 绝对值

    """
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 返回多个值
import math # import math 包

def move(x, y, step, angle=0):
    """移动

    :x: TODO
    :y: TODO
    :step: TODO
    :angle: TODO
    :returns: TODO

    """
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)



