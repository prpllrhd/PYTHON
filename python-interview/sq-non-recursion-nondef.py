#!/usr/bin/env python
import sys
"""
this is to calculate square of a number non recursively without a function
"""
n=int(sys.argv[1])
p=int(sys.argv[2])
a=n
while p > 1:
    n=n*a
    p -= 1
print n

