#!/usr/bin/python3
""" Module to find the max integer in a list """


def max_integer(list=[]):
    """
    Function to find and return the max integer in a list of integers
    If the list is empty, the function returns None
    """

    if len(list) == 0:
        return None
    res = list[0]
    counter = 1
    while counter < len(list):
        if list[counter] > res:
            res = list[counter]
        counter += 1
    return res
