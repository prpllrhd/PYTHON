#!/usr/bin/env python
##counts occurences of a name in a list
dict={}
a=["sameer","rakhee","aai","anjali","rakhee","sameer","rakhee"]
for i in a:
    if dict.has_key(i):
        dict[i]+=1
    else:
        dict[i]=1
print dict
