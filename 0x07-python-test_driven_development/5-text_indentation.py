#!/usr/bin/python3
"""
Function that prints a text with 2 new lines after each of these characters:
. ? and :
"""


def text_indentation(text):
    """
    Function that prints 2 new lines after ".?:" characters
    Args:
        text: input string
    Returns:
        No return
    Raises:
        TypeError: If text is not a string
    """

    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        else:
            counter = 0
            while counter < len(text) and text[counter] == ' ':
                counter += 1
            # Dont know what I did right here
            while counter < len(text):
                print(text[counter], end="")
                if text[counter] == "\n" or text[counter] in ".?:":
                    if text[counter] in ".?:":
                        print("\n")
                    counter += 1
                    while counter < len(text) and text[counter] == ' ':
                        counter += 1
                    continue
                counter += 1
    except Exception as exc:
        return (exc)
