#!/usr/bin/python3

''' Class Square: Definition of new type
'''


class Square:
    ''' Represents a square with a zise.
    '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Initialise instance/object
        '''
        self.size = size
        self.position = position

    def area(self):
        ''' Return the current square area
        '''
        return self.__size ** 2

    def my_print(self):
        ''' Prints square in stdout
        '''
        if self.size:
            print('\n' * self.position[1], end="")
            for i in range(self.size):
                print(' ' * self.position[0] + '#' * self.size)
        else:
            print()

    def __str__(self):
        ''' Prints square format
        '''
        if self.size:
            str = '\n' * (self.position[1])
            for i in range(self.size - 1):
                str += ' ' * self.position[0] + '#' * self.size + '\n'
            str += ' ' * self.position[0] + '#' * self.size
            return str
        return str()

    @property
    def size(self):
        ''' Return current square size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        ''' Set current square size
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        ''' Returns current square position
        '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' Sets current square position
        '''
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                isinstance(value[0], int) and
                isinstance(value[1], int) and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
