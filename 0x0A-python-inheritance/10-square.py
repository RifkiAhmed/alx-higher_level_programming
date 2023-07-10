#!/usr/bin/python3
''' Module for a class Square that inherits from Rectangle class
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    ''' Represents a Square class that inherits from Rectangle
    '''

    def __init__(self, size):
        ''' Initialises instance of class Square
        '''
        super().__init__(size,size)
        self.__size = size

    def area(self):
        ''' Calculates area of Rectangle instance
        '''
        return self.__size ** 2
