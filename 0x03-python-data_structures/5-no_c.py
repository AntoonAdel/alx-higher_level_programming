#!/usr/bin/python3
def no_c(my_string):
    clist = list(my_string)
    [clist.remove(a) for a in clist if a == 'c' or a == 'C']
    return("".join(clist))
