#!/usr/bin/python3
''' Module: Creates class Rectangle
'''


class Rectangle:
    ''' Defines an empty Rectangle class
    '''

    def __init__(self, width=0, height=0):
        ''' Initialize instance
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' Gets width value
        '''
        return with

    @width.setter
    def width(self, value):
        ''' Sets width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise Valueerror("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Gets height value
        '''
        return height

    @height.setter
    def height(self, value):
        ''' Sets height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
