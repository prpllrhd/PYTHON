#!/usr/bin/env python
def fix_start(s):
  # +++your code here+++
  start=s[0]
  end=s[1:]
  fixed=end.replace(start,"*")
  return start + fixed
print fix_start("babble")
