#!/usr/bin/env python
import re
text = """
1. ricochet robots
2. settlers of catan
3. acquire
"""
#b=re.findall(r'^(\d+)\.(.*)$', text, re.MULTILINE)
b=re.findall(r'^(\d+)\.(.*)$', text)
print b
