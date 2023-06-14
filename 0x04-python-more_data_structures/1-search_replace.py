#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list == []:
        return []
    my_list2 = my_list[:]
    for i in range(len(my_list2)):
        if my_list2[i] == search:
            my_list2[i] = replace
    return my_list2
