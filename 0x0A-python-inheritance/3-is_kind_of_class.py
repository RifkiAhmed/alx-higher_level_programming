#!/usr/bin/python3
''' Module defines a function thats checks if an object is
    an instance of the specified class or a class that inherits from
'''


def is_kind_of_class(obj, a_class):
    ''' Checks if obj is an instance of a_class or a class
        that iherits from
    '''
    return isinstance(obj, a_class)
