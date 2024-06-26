#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    function that appends a string at the end of a text file (UTF8)
    and returns the number of characters added
    """
    if filename:
        with open(filename, "a", encoding="utf-8") as my_file:
            return my_file.write(text)
