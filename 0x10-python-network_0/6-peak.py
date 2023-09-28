#!/usr/bin/python3
"""Python script that Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function definition"""
    if not list_of_integers:
        return None

    my_list = list_of_integers
    prev, lenght = 0, len(my_list)
    for i in range(0, lenght):
        if my_list[i] >= my_list[i + 1] and my_list[i] >= prev:
            return my_list[i]
        prev = my_list[i - 1]
