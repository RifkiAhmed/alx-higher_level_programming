#!/usr/bin/python3
''' Module for a class Rectangle that inherits from BaseGeometry class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry
''' BaseGeometry superclass
'''


class Rectangle(BaseGeometry):
    ''' Represents a Rectangle class that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        ''' Initialises instance of class Rectangle
        '''
        self.__width = width
        self.__height = height
        super().integer_validator("width", self.__width)
        super().integer_validator("height", self.__height)
