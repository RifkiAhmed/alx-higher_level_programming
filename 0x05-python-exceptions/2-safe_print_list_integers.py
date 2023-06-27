#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n_item = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
        except TypeError:
            n_item -= 1
        except ValueError:
            n_item -= 1
        n_item += 1
    print('')
    return n_item
