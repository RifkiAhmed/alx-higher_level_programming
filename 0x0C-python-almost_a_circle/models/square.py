#!/usr/bin/python3
''' Module for Square class that inherits from rectangle class
'''
from rectangle import Rectangle


class Square(Rectangle):
    ''' Representing Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Initialize instance '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        ''' Returns a string representation of Square instance '''
        return "[Square] ({0}) {1}/{2} - {3}".format(
            self.id,
            self.x,
            self.y,
            self.width)

    @property
    def size(self):
        ''' Gets Square size '''
        return self.height

    @size.setter
    def size(self, size):
        ''' Sets size of Square '''
        self.width = size
        self.height = size
