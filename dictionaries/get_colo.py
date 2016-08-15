#!/usr/bin/python
import sys
hash = {}
f = open(sys.argv[1],"rU")
for i in f:
    SPLIT = i.split('.')
#    print SPLIT[-3]
    colo =  SPLIT[-3]
    if colo not in hash:
        hash[colo] = 1
    else:
        hash[colo] = hash[colo] + 1
for key in hash:
    print key,"===>:",hash[key]
