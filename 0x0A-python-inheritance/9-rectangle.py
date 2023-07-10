#!/usr/bin/python3
''' Module for a class Rectangle that inherits from BaseGeometry class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    ''' Represents a Rectangle class that inherits from BaseGeometry
    '''

    def __init__(self, width, height):
        ''' Initialises instance of class Rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        ''' Calculates area of Rectangle instance
        '''
        return self.__width * self.__height

    def __str__(self):
        ''' Returns a string widht/height representation of Rectange instance
        '''
        return '[Rectangle] ' + str(self.__width) + (
                '/' + str(self.__height))
