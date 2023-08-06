#!/usr/bin/python3
"""
    Rectangle module inherits from BaseGeometry module
"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ Defines Rectangle class """
    def __init__(self, width, height):
        """ Initialises Rectangle instance """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
