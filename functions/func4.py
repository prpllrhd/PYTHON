#!/usr/bin/python
import sys
def addnus(a,b):
   x=a+b
   return x    
def main():
  print addnus(int(sys.argv[1]),int(sys.argv[2]))
if __name__ == '__main__':
   main()
