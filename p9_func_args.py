#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#

# Python的函数定义非常简单，但灵活度却非常大。
# 除了正常定义的必选参数外，还可以使用默认参数、
# 可变参数和关键字参数，使得函数定义出来的接口，
# 不但能处理复杂的参数，还可以简化调用者的代码。

# 默认参数
# 默认参数应该放在必选参数后，这样才可以省略
def power(x, n=2):
    s = 1
    while n > 0:
        s = s * x
        n = n - 1
    return s

print(power(3))

# 默认参数很有用，但也有坑啊
def add_end(L=[]):
    """TODO: Docstring for add_end.

    :L: TODO
    :returns: TODO

    """
    L.append('END')
    return L

# 正常调用
print(add_end([1, 2, 3]))
print(add_end(['x', 'y', 'z']))

# 使用默认参数调用
print(add_end()) # ['END']
# but 当你在此调用时
# 就不对了
print(add_end()) # ['END', 'END']

# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！


# 下面来改一下
def add_end2(L=None):
    """add_end2

    :L: TODO
    :returns: TODO

    """
    if L is None:
        L = []
    L.append('END')
    return L

print(add_end2()) # ['END']
print(add_end2()) # ['END']

###########################################
# 可变参数
def calc(*numbers):
    """TODO: Docstring for calc.

    :numbers: TODO
    :returns: TODO

    """
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1, 2, 3))

nums = [1, 2, 3]
print(calc())
print(calc(nums[0], nums[1], nums[2]))
# *nums表示把nums这个list的所有元素作为可变参数传进去。
# 这种写法相当有用，而且很常见。
print(calc(*nums))




# 关键字参数
# 可变参数允许传入多个参数，这些参数在函数内部自动组装为 tuple.
# 而关键字参数允许你传入 0 或多个含参数名的参数。
# 这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    """TODO: Docstring for person.

    :name: TODO
    :age: TODO
    :**kw: TODO
    :returns: TODO

    """
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')

# 它可以扩展函数的功能。比如，在person函数里，
# 我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。
# 试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。


extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])

# 上面复杂的调用可以用简化的写法：
person('Jack', 24, **extra)

# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，
# kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，
# 对kw的改动不会影响到函数外的extra。
#


# 命名关键字参数

