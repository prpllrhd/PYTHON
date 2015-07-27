#!/usr/bin/env python
import sys
def nonrec(n,p):
    a = n
    while p > 1:
        n = n * a;
        p -= 1
    print n
nonrec(int(sys.argv[1]),int(sys.argv[2]))
      
