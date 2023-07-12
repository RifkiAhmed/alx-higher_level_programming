#!/usr/bin/python3
''' Module for inserting a line of text to a file
    after each line containing a specific string
'''


def append_after(filename="", search_string="", new_string=""):
    ''' Insetrs a line of text to a line after each
        line containing a specific string
    '''
    text = ""
    with open(filename, encoding="utf-8", mode="r") as file13:
        for line in file13:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, encoding="utf-8", mode="w") as file13:
        file13.write(text)
