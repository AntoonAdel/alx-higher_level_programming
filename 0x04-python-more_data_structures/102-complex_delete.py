#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for thing in list(a_dictionary):
        if a_dictionary[thing] == value:
            del a_dictionary[thing]
    return a_dictionary
