#!/usr/bin/python3
''' Module for a function that returns list of attributes
    and methods of an object
'''


def lookup(obj):
    ''' Gets a list of attributes and methods of an object
    '''
    return dir(obj)
