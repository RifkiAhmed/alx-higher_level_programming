#!/usr/bin/python3
''' Module: Creates class Rectangle
'''


class Rectangle:
    ''' Defines a Rectangle class
    '''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' Initialize instance
        '''
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        ''' Gets width value
        '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Sets width
        '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' Gets height value
        '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Sets height
        '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' Gets rectangle area
        '''
        return self.width * self.height

    def perimeter(self):
        ''' Gets rectanlge perimeter
        '''
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def __str__(self):
        ''' Gets string representation
        '''
        if self.width == 0 or self.height == 0:
            return ''
        return ('\n'.join([str(self.print_symbol) * self.width] * self.height))

    def __repr__(self):
        if self.width == 0 or self.height == 0:
            return ''
        return 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'

    def __del__(self):
        ''' Deletes the current instance
        '''
        type(self).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Gets the biggest rectangle based on the area
        '''
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        ''' Returns a new Rectangle instance with width == height == size
        '''
        return Rectangle(size, size)
