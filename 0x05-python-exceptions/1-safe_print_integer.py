#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        If_value = True
    except Exception:
        If_value = False
    return (If_value)
