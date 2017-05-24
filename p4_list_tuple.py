#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])

# 取最后一个元素，len(classmates) - 1 或倒数 -1
# 倒数第二个
print(classmates[-1])

# 追加
classmates.append('Adam')
print('append>',classmates)

# 插入到指定位置
classmates.insert(1, 'Jack')
print('insert(1)>',classmates)

# 删除末尾
classmates.pop()
print('pop()>',classmates)

# 删除指定索引位置
classmates.pop(1)
print('pop(1)>',classmates)

# 改变指定位置的值
classmates[1] = 'Sarah'
print('change value', classmates)


# list中的数据类型也可以不同
L = ['Apple', 123, True]

# list元素也可以是另一个list
s = ['python3', 'java', ['asp', 'php'], 'scheme']
print(len(s))

# 空list
m = []
print(len(m))

####################################################
# tuple 元祖，tuple一旦初始化就不能修改
# 因为tuple不可变，所以代码更安全。
# 如果可能，能用tuple代替list就尽量用tuple。
classmates = ('Michael', 'Bob', 'Tracy')

# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)

# 定义空的 tuple
t = ()
print(t)

# 定义一个元素的 tuple，必须这样写
# 不能去掉逗号，否则 t = (2) == t = 2
t = (2,)
print(t)

# 可变的 tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
