#!/usr/bin/python3
"""
    Square module
"""


class Square:
    """ Define square """
    def __init__(self, size=0):
        """ Initialises instance of Square """
        self.__size = size

    @property
    def size(self):
        """ Returns size of current square """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets value of size attributte for the current instance """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Returns the current square area """
        return self.__size ** 2

    def my_print(self):
        """ Prints in stdout the square with the character # """
        if self.__size:
            print('\n'.join(["#" * self.__size] * self.__size))
        else:
            print()
