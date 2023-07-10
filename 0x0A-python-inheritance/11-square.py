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
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError('size must be an integer')
        except ValueError:
            raise ValueError('size must be greater than 0')
        self.__size = size

    def area(self):
        ''' Calculates area of Rectangle instance
        '''
        return self.__size ** 2

    def __str__(self):
        ''' Returns a string size/size representation of Square instance
        '''
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
