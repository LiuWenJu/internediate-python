#!/usr/bin/env python
# encoding: utf-8

def profile():
    name = "Danny"
    age = 20
    return (name, age)

profile_data = profile()
print profile_data[0]

print profile_data[1]


def profile():
    name = "Danny"
    age = 20
    return name, age

a = profile()

print a[1]
print a[0]




