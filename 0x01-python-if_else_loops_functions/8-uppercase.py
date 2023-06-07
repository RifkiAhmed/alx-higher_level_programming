#!/usr/bin/python3
def uppercase(str):
    string = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(65 + (ord(c) - 97))
            string += c
        else:
            string += c
    print("{}".format(string))
