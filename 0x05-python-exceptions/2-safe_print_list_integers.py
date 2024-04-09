#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    counter = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end="")
        except (ValueError, TypeError):
            pass
        else:
            counter += 1
    print()
    return (counter)
