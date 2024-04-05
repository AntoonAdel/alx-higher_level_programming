#!/usr/bin/python3
def uppercase(str):
    for arr in range(len(str)):
        char = ord(str[arr])
        if (char >= 97) and (char <= 122):
            char -= 32
        print("{}".format(chr(char)), end="")
    print()
