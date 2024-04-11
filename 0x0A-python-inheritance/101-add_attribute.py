#!/usr/bin/python3
""" Function that adds attributes to object if possible """


def add_attribute(object, name, value):
    """ Function to add new attribute IF possible (object has __dict__()) """

    if not hasattr(object, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(object, name, value)
