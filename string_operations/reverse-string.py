#!/usr/bin/env python
def reverse(string):
  rev=[]
  l=len(string)-1
#  a=string.split()
  while l>=0:
    l-=1
    rev.append(string[l])
  return ''.join(rev)
print reverse("apple is in cupertino!")
