#!/usr/bin/python3
"""
    Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """ Defines Rectangle class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialises Rectangle instance """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns the width of current rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets value of the width for current rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ returns the height of current rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets value of the height for current rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ returns the x of current rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets value of the x for current rectangle """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ returns the y of current rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets value of the y for current rectangle """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area of current rectangle """
        return self.width * self.height

    def display(self):
        """ Prints to stdout the current rectangle with the character '#' """
        print("\n".join(["#" * self.width] * self.height))

    def __str__(self):
        """ Returns a string representation of current rectangle """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id,
                self.x,
                self.y,
                self.width,
                self.height
                )
