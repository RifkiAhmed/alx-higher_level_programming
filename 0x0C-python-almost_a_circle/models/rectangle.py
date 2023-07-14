#!/usr/bin/python3
''' Module for Rectangle class that inherits from Base class
'''
from models.base import Base


class Rectangle(Base):
    ''' Representing Rectangle class'''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initialize instance '''
        self.width = width
        self.height = height
        self.x = x
        self.__init__(id)

# Getters properties
    @property
    def get_width():
        ''' Gets width value '''
        return self.__width

    @property
    def get_height():
        ''' Gets width value '''
        return self.__height

    @property
    def get_x():
        ''' Gets width value '''
        return self.__x

    @property
    def get_y():
        ''' Gets width value '''
        return self.__y

# Setters properties
    @set_width.setter
    def set_width():
        ''' Gets width value '''
        return self.__height

    @set_height.setter
    def set_height():
        ''' Gets width value '''
        return self.__height

    @set_x.setter
    def set_x():
        ''' Gets width value '''
        return self.__x

    @set_y.setter
    def set_y():
        ''' Gets width value '''
        return self.__y
