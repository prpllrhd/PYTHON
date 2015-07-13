#!/usr/bin/python
import os
filename=raw_input("Enter file name")
try:
   os.remove(filename)
except OSError,e:
   print "Exception. Not permitted"
