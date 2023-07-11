#!/usr/bin/python3
''' Module for appending a string at the end of a text file UTF-8
'''


def append_write(filename="", text=""):
    ''' Appends a string to a text file UTF-8
    '''
    with open(filename, encoding="utf-8", mode="a") as file2:
        return file2.write(text)
