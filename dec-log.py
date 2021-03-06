#!/usr/bin/env python
# encoding: utf-8

from functools import wraps

def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func(*args, **kwargs)

    return with_logging

@logit
def addition_func(x):
    """Do some math."""
    return x + x


result = addition_func(4)

