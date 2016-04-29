#!/usr/bin/env python
# encoding: utf-8

def add_to(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target

print add_to(42)

print add_to(32)

print add_to(21)
