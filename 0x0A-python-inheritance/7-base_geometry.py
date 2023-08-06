#!/usr/bin/python3
"""
    BaseGeometry module
"""


class BaseGeometry:
    """ Defines BaseGeometry class """
    def area(self):
        """ area() method is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates value """
        if not isinstance(value, int):
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
        self.name = value
