#!/usr/bin/env python
##function to get square of recursive number
def recret(n,p):
  num=1
  for i in range(p):
    num=num*n
  return num
print recret(2,4)
