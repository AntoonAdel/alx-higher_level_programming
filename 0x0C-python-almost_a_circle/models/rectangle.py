#!/usr/bin/python3
""" Creating arg rectangle class """


import json
from models.base import Base


class Rectangle(Base):
    """ The class Rectangle that inherits from Base """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializing the class Rectangle """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ The width of the rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setting the width of the rectangle """
        if isinstance(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ The height of the rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setting the height of the rectangle """
        if isinstance(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ The x coordinate of the rectangle """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setting the x coordinate of the rectangle """
        if isinstance(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ The y coordinate of the rectangle """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setting the y coordinate of the rectangle """
        if isinstance(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ The area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Printing the rectangle in stdout """
        for arg in range(self.y):
            print()
        for n in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """ Update the class Rectangle by overriding the __str__ method """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ Updating the rectangle """
        if args:
            for arg in range(len(args)):
                if arg == 0:
                    if isinstance(args[arg]) is not int:
                        raise TypeError("id must be an integer")
                    self.id = args[arg]
                elif arg == 1:
                    self.width = args[arg]
                elif arg == 2:
                    self.height = args[arg]
                elif arg == 3:
                    self.x = args[arg]
                elif arg == 4:
                    self.y = args[arg]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if isinstance(value) is not int:
                        raise TypeError("id must be an integer")
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ Returning the dictionary representation of the rectangle """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
