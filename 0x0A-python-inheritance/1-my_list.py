#!/usr/bin/python3
"""
    MyList module
"""


class MyList(list):
    """ Mylist class that inherits from List """
    def print_sorted(self):
        """ Prints current list in ascending sort """
        print(sorted(self))
