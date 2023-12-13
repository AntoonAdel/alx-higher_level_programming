#!/usr/bin/python3
def search_replace(my_list, search, replace):
    the_list = [replace if x == search else x for x in my_list]
    return (the_list)
