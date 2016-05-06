#!/usr/bin/env python
# encoding: utf-8


"""
for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
else:
    # Did't find anything..
    not_found_in_container()
"""

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n/x)
            break
else:
    # loop fell through without finding a factor
    print(n, 'is a prime number')
