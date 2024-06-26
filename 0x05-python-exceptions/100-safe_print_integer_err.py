#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except Exception as exc:
        print("Exception: {:s}".format(str(exc)), file=stderr)
        return (False)
    else:
        return (True)
