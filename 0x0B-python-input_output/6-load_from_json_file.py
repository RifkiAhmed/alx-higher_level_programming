#!/usr/bin/python3
''' Module for creating an object from a text file
'''
import json


def load_from_json_file(filename):
    ''' Creates an object from a text file
    '''
    with open(filename, encoding="utf-8", mode="r") as file6:
        my_obj = json.loads(file6.read())
        return my_obj
