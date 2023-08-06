#!/usr/bin/python3
"""
    add_attribute module
"""


def add_attribute(obj, name, value):
    """ Add attribute name to object """
    if "__dict__" in dir(obj):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
