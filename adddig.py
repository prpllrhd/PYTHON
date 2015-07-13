#!/usr/bin/python
'''tuples are immutable. so if you want to convert/add/delete, use lists or convert to lists to get result '''
def adddig(*nums):
  ints=[]
  a=tuple()
  for i in nums:
    ints.append(int(i))
#  return ints
  a=ints
  return sum(a)
def cars_name(name,*comment,bmw='red',ferrari='blue'):
  print ferrari,bmw,comment,name


def main():
  print adddig(1,2,3,4,5,6,7,'43')
  cars_name(samy,'this is awesome',ferrari='blue',bmw='silver')

if __name__ == '__main__':
  main()
