#!/usr/bin/python3
''' Module for reading from a text file UTF-8
'''


def read_file(filename=""):
    ''' Reads from a text file UTF-8
    '''
    with open(filename, encoding="utf-8") as file0:
        print(file0.read(), end="")
