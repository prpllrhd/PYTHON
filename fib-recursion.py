#!/usr/bin/env python
##function to print recursive fibonaci
def fib(n):
    if(n<=1):
        return 1
    else:
        return n + fib(n-1)
print fib(6)
        
 
