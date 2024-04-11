#!/usr/bin/python3
"""  Class that inherits from a list """


class MyList(list):
    """ Class that inherits from a list """

    def print_sorted(self):
        """ prints a list sorted in ascending order """
        print(sorted(self, reverse=False))
