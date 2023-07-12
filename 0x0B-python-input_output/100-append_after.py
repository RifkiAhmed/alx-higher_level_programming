#!/usr/bin/python3
'''
'''


def append_after(filename="", search_string="", new_string=""):
    '''
    '''
    text = ""
    with open(filename, encoding="utf8", mode="r") as file13:
        for line in file13:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, encoding="utf8", mode="w") as file13:
        file13.write(text)
