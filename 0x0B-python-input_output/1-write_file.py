#!/usr/bin/python3
''' Module for writing to a text file UTF-8
'''


def write_file(filename="", text=""):
    ''' Writes to a text file UTF-8
    '''
    with open(filename, encoding="utf-8", mode="w") as file1:
        return file1.write(text)
