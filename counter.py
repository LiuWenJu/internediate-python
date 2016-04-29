#!/usr/bin/env python
# encoding: utf-8

from collections import Counter

colours = (
    ('Yasoob', 'Yellow'),
    ('Ali', 'Blue'),
    ('Arham', 'Green'),
    ('Ali', 'Black'),
    ('Yasoob', 'Red'),
    ('Ahmed', 'Silver'),
)


favs = Counter(name for name, colour in colours)

print favs


with open('file.text', 'rb') as f:
    line_count = Counter(f)
print line_count
