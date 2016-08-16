#!/usr/bin/env python
for i in range(1,100):
  if i%4 == 0 and i%6 == 0:
    print i,"linkedin"
  elif i%4 == 0:
    print i,"linked"
  elif i%6 == 0:
    print i,"in"
