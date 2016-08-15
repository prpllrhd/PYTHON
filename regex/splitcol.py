#!/usr/bin/env python
import re
f=open("re.txt")
for i in f:
  b=i.strip()
  c=re.findall(r'^(\w.*?):(.*)$',b,re.M)
  print c
