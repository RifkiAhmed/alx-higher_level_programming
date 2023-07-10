#!/usr/bin/python3
''' Module defines a function add_attribute()
    adds attribute to an object
    else raise Typeerror with message: can't add new attribute
'''


def add_attribute(obj, name, value):
    ''' Adds an attribute to obj if possible
    '''
    if "__dict__" in dir(obj):
        obj.__setattr__(name, value)
    else:
        raise TypeError("can't add new attribute")
