#!/usr/bin/python3
"""
    Square module inherits from Rectangle module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Defines square class """
    def __init__(self, size):
        """ Initialises Square instance """
        try:
            super().__init__(size, size)
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be greater than 0")
        self.__size = size

    def area(self):
        """ Returns the area of current square """
        return self.__size ** 2
