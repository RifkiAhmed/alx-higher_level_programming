#!/usr/bin/python
"""
    add_attribute module
"""


def add_attribute(obj, name, value):
    """ Add attribute name to object """
    if "__dict__" in dir(obj):
        obj.name = value
    else:
        raise TypeError("can't add new attribute")
