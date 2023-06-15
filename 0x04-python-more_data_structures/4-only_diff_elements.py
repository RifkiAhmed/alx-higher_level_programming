#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    my_list = list(set_1) + list(set_2)
    my_list2 = []
    for elem in my_list:
        if elem in set_2 and elem in set_1:
            continue
        my_list2.append(elem)
    return set(my_list2)
