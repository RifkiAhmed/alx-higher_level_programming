#!/usr/bin/python3
"""
    my_int module inherits from int
"""


class MyInt(int):
    """ Defins MyInt a rebel class of int """
    def __eq__(self, value):
        """ Returns of equal operator inverted """
        return not super().__eq__(value)

    def __ne__(self, value):
        """ returns of not equal operator inverted """
        return not super().__ne__(value)
