#!/usr/bin/python3
''' Module for Rectangle class that inherits from Base class
'''
from base import Base


class Rectangle(Base):
    ''' Representing Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initialize instance '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' Gets width value '''
        return self.__width

    @property
    def height(self):
        ''' Gets height value '''
        return self.__height

    @property
    def x(self):
        ''' Gets x value '''
        return self.__x

    @property
    def y(self):
        ''' Gets y value '''
        return self.__y

    @width.setter
    def width(self, width):
        ''' Sets width value '''
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        ''' Sets height value '''
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        ''' Sets x value '''
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        ''' Sets y value '''
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
