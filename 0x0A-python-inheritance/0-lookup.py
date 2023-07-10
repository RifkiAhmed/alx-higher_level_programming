#!/usr/bin/python3
def lookup(obj):
    ''' Gets a list of attributes and methods of an object
    '''
    return list(obj.__dict__)
