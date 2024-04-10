#!/usr/bin/python3
"""
Class that creates an object Rectangle
"""


class Rectangle:
    """ Class that creates an object Rectangle """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Constructor """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        """ Method for area calculation """
        return self.width * self.height

    def perimeter(self):
        """ Method for perimeter calculation """
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """ Returns the Rectangle for printing """
        Rec_str = ""
        if self.width == 0 or self.height == 0:
            return (Rec_str)
        else:
            symbol = str(self.print_symbol)
            for test in range(self.height):
                Rec_str += "{}".format(symbol * self.__width)
                if test != (self.height - 1):
                    Rec_str += "\n"
        return Rec_str

    def __repr__(self):
        """ Method that returns Object Representation as string """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ Action when object is deleted """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")