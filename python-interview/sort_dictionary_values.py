#!/usr/bin/env python
#http://stackoverflow.com/questions/613183/sort-a-python-dictionary-by-value
# Since a dictionary can't be sorted by value, what you can do is to convert
# it into a list of tuples with tuple length 2.
# You can then do custom sorts by passing your own function to sorted().
def sortedvalues(a):
  return a[1]
def dictio(d):
#  dict={}
  return sorted(d.items(),key=sortedvalues)
scores={"sachin":192,"saurav":49,"vinod":193,"viraat":121,"rahul":210}
print dictio(scores)
