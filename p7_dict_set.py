#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# python 内置字典，也称为map
# 使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

d['Adam'] = 67
print(d)
print(d['Adam'])


# 取不存在的 key 是会报错的
# so，判断 key 是否存在字典中
ok = 'Thomas' in d
print(ok)

# 第二种取值的方法
# 如果 key 不存在会返回 None
# 活着你给的默认值
print(d.get('Thomas'))
print(d.get('Thomas', -1))


# 删除一个 key
print(d.pop('Bob'))
print(d)


# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
#
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict 是用空间来换取时间的一种方法。
#
#
#
# dict 在 Python 代码中几乎无处不在
# 正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#


# set和dict类似，也是一组key的集合，但不存储value。
# 它是无序和无重复元素的一个集合
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print(s) # {1, 2, 3}

# 重复的元素在 set 内被自动过滤
s = set([1, 1, 2, 2, 3, 3])
print(s)

# 添加 key，可重复但不会有效果
s.add(4)
print(s)
s.add((8, 9, 10))
print(s)

# 删除 key
s.remove(4)
print(s)

# 取交集
s1 = set([1, 2, 3, 4])
s2 = set([3, 4, 5])
print(s1 & s2)

# 取并集
print(s1 | s2)

