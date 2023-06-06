#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = 65 + (ord(c) - 97)
            print("{0:c}".format(c), end="")
        else:
            print("{0:s}".format(c), end="")
