#!/usr/bin/python3
"""
    Square module inherits from Rectangle module
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ Defines square class """
    def __init__(self, size):
        """ Initialises Square instance """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the area of current square """
        return self.__size ** 2 
