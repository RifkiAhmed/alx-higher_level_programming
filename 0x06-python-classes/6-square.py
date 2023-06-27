#!/usr/bin/python3

'''
class Square: new type
'''


class Square:
    ''' Represents a square with a zise and position.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialise instance/object'''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        ''' Returns current square position'''
        return self.__position

    @position.setter
    def position(self, value):
        ''' Sets current square position'''
        if not (isinstance(value, tuple)
                and isinstance(value[0], int)
                and isinstance(value[1], int)
                and len(value) == 2
                and value[0] >= 0
                and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position == value

    def area(self):
        ''' Return the current square area'''
        return self.size ** 2

    def my_print(self):
        ''' Prints in stdout the square
            if size is diffrent from 0 prints with the character #
            otherwise prints an empty line
        '''
        if self.size == 0:
            print()
        else:
            print('\n' * self.position[1], end="")
            print('\n'.join(
                [' ' * self.position[0] + '#' * self.size] * self.size
            ))
