#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_2 = [True if (num % 2) == 0 else False for num in my_list]
    return (list_2)
