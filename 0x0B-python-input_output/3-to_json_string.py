#!/usr/bin/python3
""" object to JSON string function """


import json


def to_json_string(my_obj):
    """ function that returns the JSON representation of an object (string) """
    return (json.dumps(my_obj))
