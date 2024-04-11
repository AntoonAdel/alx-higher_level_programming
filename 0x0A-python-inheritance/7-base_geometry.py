#!/usr/bin/python3
""" Geometry Class """


class BaseGeometry:
    """ Geometry Class """

    def area(self):
        """ Raise an exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates Value
        name is assumed to be a string
        """

        try:
            if type(value) != int:
                err = "{:s} must be an integer".format(name)
                raise TypeError(err)
            if value <= 0:
                err = "{:s} must be greater than 0".format(name)
                raise ValueError(err)
        except Exception as exc:
            return exc
