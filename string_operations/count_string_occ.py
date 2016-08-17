#!/usr/bin/env python
import argparse
parser=argparse.ArgumentParser()
parser.add_argument("--word")
args=parser.parse_args()
if args.word:
  f=open("/Users/samy/git/python/python-interview/file.txt")
  count=0
  for i in f:
    if args.word in i:
      count+=1
print args.word,"count:",count


