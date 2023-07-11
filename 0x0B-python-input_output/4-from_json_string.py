#!/usr/bin/python3
''' Module for an object created from JSON representation
'''
import json


def from_json_string(my_str):
    ''' Returns an object gotten from JSON represention(string)
    '''
    return json.loads(my_str)
