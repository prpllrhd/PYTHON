#!/usr/bin/env python
import re
'''
read a file and 
if you find any 
line with "From:" 
it will print it 
out. use re module
'''
f = open("re.txt")
for i in f:
  line=i.strip()
  if re.findall('From:',i):
    print line
  
