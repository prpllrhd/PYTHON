#!/usr/bin/python
dict = {}
d = "sameer IS a very nice boy he is always very efficient boy"
l=d.lower()
for i in l.split():
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] = dict[i] + 1
for key in dict:
    print "Key ==>",key,"\nValue ==>",dict[key]
