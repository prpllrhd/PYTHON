#!/usr/bin/env python
import re
f=open("re.txt")
for o in f:
  i=o.strip()
  a=re.sub("\w+:","REPLACED",i,re.M)
  print a
  
