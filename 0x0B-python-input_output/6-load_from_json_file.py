#!/usr/bin/python3
""" Create object from JSON file  """


import json


def load_from_json_file(filename):
    """ function that creates an Object from a JSON file """

    if filename:
        with open(filename, "r", encoding="utf-8") as my_file:
            return json.load(my_file)
