#!/usr/bin/env python
# encoding: utf-8

def hi(name="yasoob"):
    return "hi " + name

print hi()

greet = hi

print greet()

del hi

try:
    print hi()

    print greet()
except:
    pass

