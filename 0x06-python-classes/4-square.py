#!/usr/bin/python3

'''
class Square: new type
'''


class Square:
    ''' Represents a square with a zise.'''

    def __init__(self, size=0):
        '''Initialise instance/object'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        ''' Return the current square area'''
        return self.__size ** 2

    @property
    def size(self):
        ''' Return current square size'''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Set current square size'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
