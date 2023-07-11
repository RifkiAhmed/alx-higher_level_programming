#!/usr/bin/python3
''' Module for an class BaseGeometry
'''


class BaseGeometry(object):
    ''' Represents a BaseGeometry class
    '''

    def area(self):
        '''  Gets area of current instance or raise Exception
        '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' Validates value; value must be an integer and greater than 0
        '''
        if type(value) is not int:
            raise TypeError(str(name) + ' must be an integer')
        elif value <= 0:
            raise ValueError(str(name) + ' must be greater than 0')
        else:
            self.name = value
