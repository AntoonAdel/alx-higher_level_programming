#!/usr/bin/python3
""" Add all arguments to a list and save them to a .json """


from sys import argv
from os import path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

file_name = "add_item.json"

if path.isfile(file_name):
    lst = load_from_json_file(file_name)
else:
    lst = []

for test in range(1, len(argv)):
    lst.append(argv[test])

save_to_json_file(lst, file_name)
