#!/usr/bin/python3
"""
Class that creates a Rectangle Object
"""


class Rectangle:
    """ Class that creates a Rectangle Object """

    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Width Getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ Width Setter """
        if not isinstance(value, int):
            err = "width must be an integer"
            raise TypeError(err)
        if (value < 0):
            err = "width must be >= 0"
            raise ValueError(err)
        self.__width = value

    @property
    def height(self):
        """ Height Getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ Height Setter """
        if not isinstance(value, int):
            err = "height must be an integer"
            raise TypeError(err)
        if (value < 0):
            err = "height must be >= 0"
            raise ValueError(err)
        self.__height = value
