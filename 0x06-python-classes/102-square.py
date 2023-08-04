#!/usr/bin/python3
"""
    Square module
"""


class Square:
    """ Define square """
    def __init__(self, size=0):
        """ Initialises instance of Square """
        self.size = size

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
        return self.size ** 2

    def __lt__(self, square_2):
        """ Checks if current square area is less than square_2 area """
        return self.area() < square_2.area()

    def __le__(self, square_2):
        """ Checks if current square area less/equal to square_2 area """
        return self.area() <= square_2.area()

    def __eq__(self, square_2):
        """ Checks if area of current square and square_2 are equals """
        return self.area() == square_2.area()

    def __ne__(self, square_2):
        """ Checks if area of current square and square_2 are not equals """
        return self.area() != square_2.area()

    def __gt__(self, square_2):
        """ Checks if current square area is greater than square_2 area """
        return self.area() > square_2.area()

    def __ge__(self, square_2):
        """ Checks if current square area greater/equal to square_2 area """
        return self.area() >= square_2.area()
