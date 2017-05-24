#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 第一种
# for...in 循环，可一次把 list 或 tuple 中的
# 每个元素迭代出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range() 函数，可以生成一个整数序列（从0开始）
# 通过 list() 可以转为 list
l = list(range(5))
print(l)


# 第二种
# while 循环，只要条件满足，就不断循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


# break 跳出循环
n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')


# continue 跳过当前循环，继续下次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
