#!/usr/bin/python3
def common_elements(set_1, set_2):
    my_list = []
    for elem in set_1:
        for elem2 in set_2:
            if elem == elem2:
                my_list.append(elem)
                continue
    return set(my_list)
