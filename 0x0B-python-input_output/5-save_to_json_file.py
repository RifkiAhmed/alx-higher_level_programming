#!/usr/bin/python3
''' Module for writing JSON representation of an object
    to a text file
'''
import json


def save_to_json_file(my_obj, filename):
    ''' Writes JSON representation of an object to a text file
    '''
    with open(filename, encoding="utf-8", mode="w") as file5:
        file5.write(json.dumps(my_obj))
