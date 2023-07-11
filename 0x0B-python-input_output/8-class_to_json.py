#!/usr/bin/python3
''' Module for writing dictionary representation of a class object
'''


def class_to_json(obj):
    ''' Writes dictionary representation of a class object
    '''
    return obj.__dict__
