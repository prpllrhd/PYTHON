#!/usr/bin/python
import sys
def addnus(a,b):
   x=a+b
   print x    
   y=a*b
   print y
def main():
   addnus(int(sys.argv[1]),int(sys.argv[2]))
if __name__ == '__main__':
   main()
