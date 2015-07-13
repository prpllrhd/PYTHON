#!/usr/bin/python
import argparse
parser=argparse.ArgumentParser()
parser.add_argument('-ho','--hostname',required=True,help='hostname')
args=parser.parse_args()
if args.hostname:
  a=args.hostname
  print a
