#!/usr/bin/python3
for char in range(122, 96, -1):
    if char % 2:
        char -= 32
    print("{}".format(chr(char)), end="")
    if char % 2:
        char += 32
