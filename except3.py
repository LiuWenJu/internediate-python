#!/usr/bin/env python
# encoding: utf-8

try:
    file = open('test.txt', 'rb')
except Exception:
    # print some logs, if you want
    raise
