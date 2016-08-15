#!/usr/bin/python
import sys
def count():
    words="he is a GOOD boy doing good work and is very intelligent and is very smart"
    hash = {}
    lower=words.lower()
    swords =  lower.split()
    print hash
    for i in swords:
        if i not in hash:
            hash[i] = 1
        else:
            hash[i] = hash[i] + 1
    for key in hash:
        print key, "==>",hash[key]
def main():
    count()
if __name__ == '__main__':
    main()
