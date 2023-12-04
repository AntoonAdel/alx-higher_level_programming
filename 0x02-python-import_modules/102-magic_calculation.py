#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        result = add(a, b)
        for num in range(4, 6):
            result = add(result, num)
        return result
    else:
        return sub(a, b)
