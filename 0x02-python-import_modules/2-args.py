#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print(f"{count:d} arguments.")
    elif count == 1:
        print(f"{count:d} arguments.")
    else:
        print(f"{count:d} arguments.")
    for a in range(0, len(argv)):
        if a > 0:
            print(f"{a:d}: {argv[a]:s}")
