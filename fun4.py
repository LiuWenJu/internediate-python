#!/usr/bin/env python
# encoding: utf-8

def hi():
    return "hi yasoob!"

def doSomethingBeforeHi(func):
    print "I am doing some boring work before executing hi()"
    print func()

doSomethingBeforeHi(hi)
