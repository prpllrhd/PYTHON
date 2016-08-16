#!/usr/bin/env python
"""
input any number between (1-10) and output prints if its divisible and also prints all other numbers unto it if not divisible. ( say input 5 prints - 1,2,4)
"""
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('number')
args=parser.parse_args()
num=int(args.number)
div=[]
nondiv=[]
if num <1 or num>10:
  print "Ok"
else:
  r=range(1,num+1)
  for i in r:
    if num%i==0:
      div.append(i)
    else:
      nondiv.append(i)
print "divisible by number",div
print "not divisible by number",nondiv

