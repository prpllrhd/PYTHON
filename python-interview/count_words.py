#!/usr/bin/env python
import sys,argparse
parser=argparse.ArgumentParser()
#parser.add_argument('-f','--file',type=String,Required=True,help="file to open")
parser.add_argument('-f','--file',required=True,help="file to open")
parser.add_argument('count',help="counting number of occurenses of each number")
args=parser.parse_args()
def count_words(file):
  dict={}
  f=open(file,"r")
  a=f.readline().split()[0]
  for i in a:
    if dict.has_key(i):
      dict[i]+=1
    else:
      dict[i]=1
  print  dict
def main():
  if args.count:
    count_words(args.file)

if __name__ == "__main__":
  main()
