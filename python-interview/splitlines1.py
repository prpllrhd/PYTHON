#!/usr/bin/env python
import re
def convertcoma(file):
    fn=open(file,'r')
    for i in fn:
        b = i.strip()
#        a = re.sub('\n+|\s+|\t+',' ',b)
        print b,


convertcoma('splitlines1.txt')
