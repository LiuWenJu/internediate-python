#!/usr/bin/env python
# encoding: utf-8

add = lambda x, y: x + y
# lambda args:do(args)

print add(3, 5)

a = [(1, 2), (4, 1), (9, 10), (13, -3)]
a.sort(key=lambda x: x[1])

print a

list1 = [1, 2, 3]
list2 = [5, 6, 7]
data = zip(list1, list2)
data.sort()

list1, list2 = map(lambda t: list(t), zip(*data))
