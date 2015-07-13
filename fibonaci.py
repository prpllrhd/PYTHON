#!/usr/bin/python
def fib(n):
   result=[]
   x,y=0,1
   while x<n:
      result.append(x)
      x,y=y,x+y
   return result
print fib(100)
