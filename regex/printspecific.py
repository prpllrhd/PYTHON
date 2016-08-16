#!/usr/bin/env python
import re
string="00:00:00 Mar 1 this host host100 died. Call 408-555-1111"
"""
print out Mar 1, host100 and 555-1111
"""
#a=re.findall(r"\d+:\d+:\d+\s*([A-Z]\w+\s+\d+)\s+\w+\s+\w+\s+([a-z0-0]+)\s+\w+\.\s+[A-Z][a-z]+\s+\d{1,3}-(\d{3}-\d{4})",string,re.M)
a=re.findall(r"\d+:\d+:\d+\s*([A-Z]\w+\s+\d+).*",string)
print a
