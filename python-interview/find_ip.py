#!/usr/bin/env python
import re
f = open("ip.txt")
fip = []
findip = re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",re.MULTILINE)
dict = {}
for i in f.readlines():
   print  re.findall(findip,i)
   if dict.has_key(fip):
     dict[fip]+=1
   else:
     dict[fip]=1
print dict
