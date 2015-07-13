#!/usr/bin/env python
###recursive function to calculate square

#def rec(pow):
#    num=2
#    if pow >=1:
#        return num * rec(pow-1)
#    else:
#        return 1
#print rec(4)
def rec(num,pow):
    if pow>=1:
        return num * rec(num,pow-1)
    else:
        return 1
print rec(6,3)
