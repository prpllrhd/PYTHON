#!/usr/bin/python
#example:lists, appending unique items from a list to a list
list=["samy","rakhee","yuvi","rakhee","ravi","rakhee","samy"]
b=[]
#for d in set(list):
#  print d
print type(list)
for i in list:
  if i in b:
    next
  else:
    b.append(i)
print b
