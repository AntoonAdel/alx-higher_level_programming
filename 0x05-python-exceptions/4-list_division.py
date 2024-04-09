#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_new_list = []
    for Len in range(list_length):
        try:
            division = my_list_1[Len] / my_list_2[Len]
        except Exception as exc:

            if isinstance(exc, ZeroDivisionError):
                print("division by 0")

            elif isinstance(exc, TypeError):
                print("wrong type")

            elif isinstance(exc, IndexError):
                print("out of range")

            division = 0

        finally:
            my_new_list.append(division)

    return (my_new_list)
