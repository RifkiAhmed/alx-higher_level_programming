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
        return self.__size ** 2
