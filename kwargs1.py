#!/usr/bin/python
def kwargs1(**kwargs):
  for key in kwargs:
    print "%s: %s" %(key,kwargs[key])
def main():
  kwargs1(sameer='38',rakhee='33',yuvaraaj='8')

if __name__ == '__main__':
  main()
