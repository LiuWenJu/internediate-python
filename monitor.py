#!/usr/bin/env python
# encoding: utf-8

import time

def getMen():
    with open('/proc/meminfo') as f:
        total = int(f.readline().split()[1])
        free = int(f.readline().split()[1])
        memavailable = int(f.readline().split()[1])
        buffers = int(f.readline().split()[1])
        cache = int(f.readline().split()[1])
    men_use = total-free-buffers-cache
    print men_use/1024
    print memavailable/1024
while True:
    time.sleep(1)
    getMen()
