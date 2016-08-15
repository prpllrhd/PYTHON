#!/usr/bin/env python
import re
f=open("file1.txt")
dict={}
for i in f:
  b=i.split()[0]
  if dict.has_key(b):
    dict[b]+=1
  else:
    dict[b]=1
print dict
