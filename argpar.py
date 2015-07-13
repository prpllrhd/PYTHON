#!/usr/bin/python
import os
import argparse
parser=argparse.ArgumentParser(description='this is help')
parser.add_argument("-p","--ping",nargs="+",help="this is detailed help")
args=parser.parse_args()
if args.ping:
  for u in args.ping:
  #print "This is the help i was referring to"+args.API
    os.system("ping -c 3" +" "+ u)
