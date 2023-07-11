#!/usr/bin/python3
''' Module for JSON representation of an object
'''
import json


def to_json_string(my_obj):
    ''' Returns JSON represention(string) of an object
    '''
    return json.dumps(my_obj)
