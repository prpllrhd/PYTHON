#!/usr/bin/python
"""
example:positional_argument
example:optional_argument
positional argument is must but optional argument is optional.
"""
import argparse
a=argparse.ArgumentParser()

##optional arguments
a.add_argument('-int','--integer',type=int,nargs='+')

##positional arguments
a.add_argument('host')
args=a.parse_args()
if args.integer:
    c=sum(args.integer)
    print c
elif args.host:
    d=args.host
    print d
