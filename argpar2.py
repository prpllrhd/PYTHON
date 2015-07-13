#!/usr/bin/python
import os
import argparse
parser=argparse.ArgumentParser(description='this is initial help')  ##this is instantiating the module
parser.add_argument("-v","--volume",help='this is detailed help.' \
 		   'Here you will find complete documentation on this feature')
args=parser.parse_args()
if args.volume:
  print os.environ['USER']
  os.chdir('/Users/samy/a')
  print os.getcwd()
  print os.getlogin()
  print os.environ['SHELL'].split('/',2)[1]
