#!/usr/bin/python3
""" Class that inherits from int """


class MyInt(int):
    """ MyInt class with != and == interchanged """

    def __eq__(self, other):
        """ Super Call to Not Equal """
        return self.real != other

    def __ne__(self, other):
        """ Super Call to Equal """
        return self.real == other
