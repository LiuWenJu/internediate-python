#!/usr/bin/env python
# encoding: utf-8

from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print "I am doing some boring work before execting a_func()"
        a_func()
        print "I am doing some boring work after execting a_func()"

    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    """Hey yo! Decorate me!"""
    print ("I am the function which needs some decoration to " "remove my foul smell ")


print a_function_requiring_decoration.__name__
