#!/usr/bin/env python
def get_last(listed):
  return listed[1]
a=[('aaz',3),('bbfdddd',4),('aaa',14),('ddddddddddddddd',1),('dcfs',4)]
print sorted(a,key=get_last)
