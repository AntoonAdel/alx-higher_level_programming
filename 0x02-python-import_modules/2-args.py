#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    counter = len(argv) - 1
    if counter == 0:
        print("{:d} arguments.".format(counter))
    elif counter == 1:
        print("{:d} argument:".format(counter))
    else:
        print("{:d} arguments:".format(counter))
    for a in range(0, len(argv)):
        if a > 0:
            print("{:d}: {:s}".format(a, argv[a]))
