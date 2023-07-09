#!/usr/bin/python3
''' Module: LockedClass;
    with no class or instance attributes;
    prevents user from dynamically creating instance attributes;
    except if the new instance attribute is called first_name.
'''


class LockedClass:
    ''' Defines LockedClass
    '''
    __slots__ = ['first_name']

    def __init__(self, first_name=None):
        self.first_name = first_name
