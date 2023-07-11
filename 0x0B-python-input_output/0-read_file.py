#!/usr/bin/python3
''' Module for reading a text file UTF-8
'''


def read_file(filename=""):
    ''' Reads a text file UTF-8
    '''
    with open(filename, encoding="utf-8") as text:
        print(text.read(), end="")
