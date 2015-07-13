#!/usr/bin/python
#example:dictionary. increments value by 1 on increment of key
names=['samy','rahul','samy','rakhee']
dict={}
for i in names:
  if dict.has_key(i):
    dict[i]+=1
  else:
    dict[i]=1
print dict


