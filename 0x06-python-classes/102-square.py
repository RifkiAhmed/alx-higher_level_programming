#!/usr/bin/python3

'''
class Square: new type
'''


class Square:
    ''' Represents a square with a zise.'''

    def __init__(self, size=0):
        '''Initialise instance/object'''
        self.__size = size

    def area(self):
        ''' Return the current square area'''
        return self.__size ** 2

    def __lt__(self, other):
        ''' Checks if current instance area is less than
            other instance area
        '''
        return self.area() < other.area()

    def __le__(self, other):
        ''' Checks if current instance area is less than
            or equal to other instance area
        '''
        return self.area() <= other.area()

    def __eq__(self, other):
        ''' Checks if areas of current and other instances are equals
        '''
        return self.area() == other.area()

    def __ne__(self, other):
        ''' Checks if areas of current and other instances are not equals
        '''
        return self.area() != other.area()

    def __gt__(self, other):
        ''' Checks if current instance area is greater than
            other instance area
        '''
        return self.area() > other.area()

    def __ge__(self, other):
        ''' Checks if current instance area is greater than
            or equal to other instance area
        '''
        return self.area() >= other.area()

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
