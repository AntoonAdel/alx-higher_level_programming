#!/usr/bin/python3
""" JSON to string object function """


import json


def from_json_string(my_str):
    """
    function that returns an object (Python data structure) represented
    by a JSON string
    """
    if my_str:
        return (json.loads(my_str))
