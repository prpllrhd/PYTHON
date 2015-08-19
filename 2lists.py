#!/usr/bin/env python
a=[]
b=[]
for i in range(20):
  if i%3 == 0:
    a.append(i)
  else:
    b.append(i)
c= a,b
print c
