#!/usr/bin/python3
"""
    Rectangle module
"""


class Rectangle:
    """ Defines Rectangle """
    def __init__(self, width=0, height=0):
        """ Initailises Rectangle instance """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Returns width of current rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets value of width for current rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Returns height of current rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets value of height for current rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of current rectangle """
        return self.width * self.height

    def perimeter(self):
        """ Returns perimeter of current rectangle """
        return (self.width + self.height
                ) * 2 if self.width * self.height else 0

    def __str__(self):
        """ Returns current rectangle format with the character '#' """
        if self.width and self.height:
            return '\n'.join(['#' * self.width] * self.height)
        else:
            return ''
