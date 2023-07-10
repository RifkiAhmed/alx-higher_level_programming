#!/usr/bin/python3
''' Module defines a function thats checks if the an object is exactly
    an instance of the specified class
'''


def is_same_class(obj, a_class):
    ''' Checks if obj is exactly an nstance of a_class
    '''
    return type(obj) is a_class
