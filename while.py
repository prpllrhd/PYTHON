#! /usr/bin/python
def print_a(a):
   b=[]
   while a<10:
      b.append('hello'+str(a))
      a+=1
   return b
print print_a(2)
