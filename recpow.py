#!/usr/bin/env python
def recur(num,pow):
    if pow>1:
        print "pow originally:",pow
        a=1
        a=a*num
        pow-=1
        print "pow now :",pow
    else:
        return 1
    return a
print recur(2,6)
        
