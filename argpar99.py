#!/usr/bin/python
"""
example:argparse
example:split
example:join
"""
import argparse
parser=argparse.ArgumentParser(description='this is help')
parser.add_argument('-ho','--hostname',required='True',help='this is from add_arg')
args=parser.parse_args()
if args.hostname:
   #name='.'.join(args.hostname.split('.')[2:5])
    """
    split examples
    """
    #name=args.hostname.split('.')
    #name=args.hostname.split('.')[2:5]
    """
    joint examples
    """
    name='.'.join(args.hostname.split('.')[2:5])
    print name
