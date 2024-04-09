#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if not my_list or x == 0:
        print()
        return (0)
    try:
        for num in range(x):
            print(my_list[num], end="")
    except:
        num -= 1
    finally:
        print()
        return(num + 1)
