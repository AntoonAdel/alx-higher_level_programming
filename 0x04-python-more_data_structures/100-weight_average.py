#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    x = sum(a[0] * a[1] for a in my_list)
    y = sum(t[1] for t in my_list)
    return (x / y)
