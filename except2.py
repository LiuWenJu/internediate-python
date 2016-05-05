#!/usr/bin/env python
# encoding: utf-8

try:
    file = open('test.txt', 'rb')
except EOFError as e:
    print "An EOFError occurred."
    raise e
except IOError as e:
    print "An error occurred."
    raise e

