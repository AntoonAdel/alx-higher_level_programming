#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout """
    if filename:
        with open(filename, encoding="utf-8") as my_file:
            print(my_file.read(), end="")
