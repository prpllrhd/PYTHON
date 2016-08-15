#!/usr/bin/env python
import re
text = """
1. sameer rakhee aai
2. ketan nilam madhavi
3. srikant manjiri mom
"""
#b=re.findall(r'^(\d+)\.\s*([a-z]+)\s*([a-z]+)\s*([a-z]+)$',text)
b=re.findall(r'^(\d*)\.\s([a-z]+)\s([a-z]+)\s([a-z]+)$',text,re.M)
print b
