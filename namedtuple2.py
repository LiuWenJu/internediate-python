#!/usr/bin/env python
# encoding: utf-8

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
perry = Animal(name="perry", age=31, type="cat")

print perry._asdict()
