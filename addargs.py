#!/usr/bin/python
import argparse
import sys
parser = argparse.ArgumentParser( description='sum the integers at the command line')
parser.add_argument( 'integers', metavar='int', nargs='+', type=int, help='an integer to be summed')
parser.add_argument( '--log1', default=sys.stdout, type=argparse.FileType('w'), help='the file where the sum should be written')
parser.add_argument('-v','--verbose',help="this is verbose")
args = parser.parse_args()
args.log1.write('%s\n' %sum(args.integers))
args.log1.close()
