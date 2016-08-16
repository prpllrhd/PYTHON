#!/usr/bin/env python
f=open("file1.txt")
i=[l.strip() for l in f]
for a in i:
  d=0
  for a in i:
    b=a.split()
    d+=1
    if d%2!=0:
      print b
