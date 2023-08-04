#!/usr/bin/python3
"""
    Square module
"""


class Square:
    """ Define square """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialises instance of Square """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Returns the size of current square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets value of size attribute of current square """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Returns the position of current square """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets values of position attribute of current square"""
        if not (isinstance(value, tuple) and len(value) == 2
                and isinstance(value[0], int) and isinstance(value[1], int)
                and value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the area of the current square """
        return self.size ** 2

    def my_print(self):
        """ Prints in stdout the current square with the character # """
        if self.size:
            print('\n' * self.position[1], end="")
            print('\n'.join(
                [' ' * self.position[0] + "#" * self.size] * self.size))
        else:
            print()
