#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nums in matrix:
        space = ""
        for num in nums:
            print("{:s}{:d}".format(space, num), end="")
            space = " "
        print()
