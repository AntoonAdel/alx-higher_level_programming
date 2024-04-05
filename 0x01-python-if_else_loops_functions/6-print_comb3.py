#!/usr/bin/python3
for digit1 in range(0, 9):
    for digit2 in range(1, 10):
        if digit2 > digit1:
            if digit1 != 8:
                print("{}{}, ".format(digit1, digit2), end="")
            else:
                print("{}{}".format(digit1, digit2))
