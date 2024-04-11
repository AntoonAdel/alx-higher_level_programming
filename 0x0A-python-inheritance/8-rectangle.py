#!/usr/bin/python3
""" Rectangle Class that inherits from BaseGeometry """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class to define object Rectangle from BaseGeometry inheritance """

    def __init__(self, width, height):
        """ Constructor """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
