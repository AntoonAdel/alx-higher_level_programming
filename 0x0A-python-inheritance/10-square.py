#!/usr/bin/python3
""" Class that inherits from Rectangle """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Represent a square """

    def __init__(self, size):
        """ Constructor """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
