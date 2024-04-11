#!/usr/bin/python3
""" script that reads stdin line by line and computes metrics """


import sys


def print_stats(dic, size):
    """ Prints information """
    print("File size: {:d}".format(size))
    for test in sorted(dic.keys()):
        if dic[test] != 0:
            print("{}: {:d}".format(test, dic[test]))


stats = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0,
         "404": 0, "405": 0, "500": 0}

counter = 0
size = 0

try:
    for line in sys.stdin:
        if counter != 0 and counter % 10 == 0:
            print_stats(stats, size)

        st_list = line.split()
        counter += 1

        try:
            size += int(st_list[-1])
        except Exception:
            pass

        try:
            if st_list[-2] in stats:
                stats[st_list[-2]] += 1
        except Exception:
            pass
    print_stats(stats, size)

except KeyboardInterrupt:
    print_stats(stats, size)
    raise
