#!/usr/bin/env python
import urllib2
response = urllib2.urlopen('http://google.com.com')
html = response.read()
for a in html:
    print a
