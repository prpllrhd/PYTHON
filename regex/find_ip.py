#!/usr/bin/env python
import re
string="this is ip 19.234.43.4 and this is not an ip 23.44"
a = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
b = re.search(a,string)
print type(b)
print b.group()
another="this is ip 134.24.2.55 and this is date 03-43-33-44"
#b=re.search(r'\d[1-254]{1,3}.\d[1-255]{1,3}.\d[1-255]{1,3}.\d[1-254]{1,3}',another)
b=re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',another)
print b
match_search="this is sameer"
b=re.search("sameer",match_search)
print b.group()
