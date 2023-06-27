#!/usr/bin/python3

'''
class Square: new type
'''


class Square:
    ''' Represents a square with a zise.'''

    def __init__(self, size=0):
        '''Initialise instance/object'''
        if size < 0:
            raise ValueError("size must be >= 0")
        if size is not int:
            raise TypeError("size must be an integer")
        self.__size = size
