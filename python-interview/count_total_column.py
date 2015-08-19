#!/usr/bin/env python
f=open("splitlines.txt","r")
sum=0
for i in f:
  cols=i.split('\t')[2]
  sum += int(cols)
print sum

