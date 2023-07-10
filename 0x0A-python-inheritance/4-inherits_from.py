#!/usr/bin/python3
''' Module defines a function thats checks if an object is
    an instance of of a class that inherits directly or not
    from a specified class
'''


def inherits_from(obj, a_class):
    ''' Checks if obj is an instance of a_class
        that inherits directly or not from the
        specified class
    '''
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
