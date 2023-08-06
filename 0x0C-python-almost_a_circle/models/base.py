#!/usr/bin/python3
"""
    Base module
"""


class Base:
    """ Defines class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initilaises Base instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
