#!/usr/bin/env python
# encoding: utf-8

# generator version

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a+b


for x in fibon(1000000):
    print x
