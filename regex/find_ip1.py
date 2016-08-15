#!/usr/bin/env python
import re
d = {}
f = open("hadoop-resourcemanager-jetty.log.2016_04_09")
findip=re.compile(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}")
for i in f.readlines():
  a=re.search(findip,i)
  print type(a)
  if d.has_key(a.group()):
    d[a.group()]+=1
  else:
    d[a.group()]=1
#  print a.group()
f.close()
print d
