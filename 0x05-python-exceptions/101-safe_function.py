#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        result = fct(*args)
    except Exception as exc:
        print("Exception: {:s}".format(str(exc)), file=stderr)
        return None
    else:
        return (result)
