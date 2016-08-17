#!/usr/bin/env python
list=[1,2,3,4,2,1,2,2,4,4,1,4,5,6,3]
z=len(list)-1
x=0
while x<=z:
  c=[]
  a=list[x]
  b=list[x+1:]
  if a not in b:
    c.append(a)
    for f in c:
      print f
  x+=1
