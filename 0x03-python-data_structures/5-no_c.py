#!/usr/bin/python3
def no_c(my_string):
    no_c_list = list(my_string)
    for cC in no_c_list:
        if cC == 'C' or cC == 'c':
            no_c_list.remove(cC)
    return ("".join(no_c_list))
