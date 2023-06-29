#!/usr/bin/python3
'''class MagicClass: definition of class
    that do the same as a given python bytecode
'''


class MagicClass:
    ''' Definition of class MagicClass
    '''
    def __init__(self, radius):
        ''' Initialisation of current instance
        '''
        self.__radius = 0
        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        ''' Returns the area of current instance
        '''
        return self.__radius ** 2 * math.pi

    def circumference(self):
        ''' Returns the circumference of current instance
        '''
        return 2 * math.pi * self.__radius
