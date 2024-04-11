#!/usr/bin/python3
""" Insert a string of text, after each line matching the search term """


def append_after(filename="", search_string="", new_string=""):
    """
    Insert <new_string> after everly line that has <search_string>
    Args:
        filename(str) -> Name of the file
        search_string(str) -> string to match
        new_string(str) -> string to append
    """

    txt_string = ""

    with open(filename) as file_read:
        for line in file_read:
            txt_string += line
            if search_string in line:
                txt_string += new_string
    with open(filename, "w") as file_write:
        file_write.write(txt_string)
