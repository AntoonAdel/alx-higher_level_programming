#!/usr/bin/python3
def no_c(my_string):
    no_c_list = list(my_string)
    [no_c_list.remove(cC) for cC in no_c_list if cC == 'c' or cC == 'C']
    return("".join(no_c_list))
