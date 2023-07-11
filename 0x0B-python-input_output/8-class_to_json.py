#!/usr/bin/python3
''' Module for writing dictionary representation of a class object
'''
import json


def class_to_json(obj):
    ''' Writes dictionary representation of a class object
    '''
    s = json.dumps(obj.__dict__)
    return json.loads(s)
