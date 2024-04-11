#!/usr/bin/python3
""" Base class """


class BaseGeometry:
    """ BaseGeometry as the base class """

    def area(self):
        """ Raise an exception """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates Value name is assumed to be a string
        """

        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
