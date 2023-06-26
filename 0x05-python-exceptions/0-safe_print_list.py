#!/usr/bin/python3
safe_print_list(my_list=[], x=0):
    n_item = 0
    try:
        for item in range(x):
            print("{}".format(my_list[item]), end="")
            n_item += 1
        print('')
        return n_item
    except:
        print('')
        return n_item
