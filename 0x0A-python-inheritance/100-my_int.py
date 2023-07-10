#!/usr/bin/python3
''' Module to defines a MyInt class that inherits from int class
    MyInt is a rebel class
'''


class MyInt(int):
    ''' Represents a rebel MyInt class that inherits from int class
    '''

    def __eq__(self, other):
        ''' Checks if equals and returns the opposite value
        '''
        if self.numerator == other.numerator:
            return False
        return True

    def __ne__(self, other):
        ''' Checks if not equals and returns the opposite value
        '''
        if self.numerator != other.numerator:
            return False
        return True
