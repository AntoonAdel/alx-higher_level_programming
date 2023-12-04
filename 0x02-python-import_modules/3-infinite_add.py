#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    for num in range(0, len(argv)):
        if num > 0:
            total += int(argv[num])
    print("{:d}".format(total))
