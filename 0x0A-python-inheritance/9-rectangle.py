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

    def area(self):
        """ Returns the area of current rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns a string representation of current rectangle """
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
