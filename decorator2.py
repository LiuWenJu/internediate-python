#!/usr/bin/env python
# encoding: utf-8

@a_new_decorator
def a_function_requiring_decoration():
    """Hey you! Decorate me!"""
    print ("I am the function which needs some decoration to "
        "remove my foul smell")

a_function_requiring_decoration()

a_function_requiring_decoration = a_new_decorator(a_function_requiring_decoration)
