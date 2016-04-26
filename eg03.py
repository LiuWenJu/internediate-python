#!/usr/bin/env python
# encoding: utf-8

def generator_function():
    for i in range(10):
        yield i

for item in generator_function():
    print item
