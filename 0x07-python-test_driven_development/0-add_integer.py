#!/usr/bin/python3
"""
    integer addition module
    a and b must be integers or float
    else raise a TypeError with message
    if a or b is float it first casted to integer
"""


def add_integer(a, b=98):
    """ Function that adds two integers a and b """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
