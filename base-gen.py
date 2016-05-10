#!/usr/bin/env python
# encoding: utf-8

from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()



with open_file('some_file') as f:
    f.write('hola!')
