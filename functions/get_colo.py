#!/usr/bin/python
import sys
def colo_count(FILE):
    hash = {}
    f = open(FILE,"rU")
    for i in f:
        SPLIT = i.split('.')
        colo = SPLIT[-3]
        if colo not in hash:
            hash[colo] = 1
        else:
            hash[colo] = hash[colo] + 1
    for key in hash:
        print  key,"===>: ",hash[key]

def main():
    colo_count(sys.argv[1])

if __name__ == '__main__':
    main()
