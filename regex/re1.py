#!/usr/bin/env python
f=open("re.txt")
for line in f:
  line=line.rstrip()
  if line.find('From:')>=0:
    print line

