#!/home/y/bin64/python
import string
ip = raw_input('Enter IP')
a = ip.split('.')
b = hex(int(a[0]))[2:].zfill(2) + hex(int(a[1]))[2:].zfill(2) + hex(int(a[2]))[2:].zfill(2) + hex(int(a[3]))[2:].zfill(2)
b = b.replace('0x', '')
b = b.upper()
print b
