#!/usr/bin/env python
import re
'''
splitprint()
take a filename as input and read all lines and split the output and print only column1
'''
def splitprint(file):
    fn=open(file,'r')
    for i in fn:
        cols=i.split('\t')[0]
        print cols

def colcal(file):
    fn=open(file,'r')
    tot=0
    for i in fn:
        cols = i.split('\t')[2]
#        tot = sum(int(cols)) ##does not work. 
        tot += int(cols)
    print"total for the column: ", tot

'''
read a file and convert all spaces,new lines to comma seperated.
'''
def convertcoma(file):
    fn=open(file,'r')
#    fn2=open(file2,'w')
    for i in fn:
        a = re.sub('\n|\s+|\t+',' ',i) 
        print a,


splitprint('splitlines.txt')

colcal('splitlines.txt')

convertcoma('splitlines1.txt')

