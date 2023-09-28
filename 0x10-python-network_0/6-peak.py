#!/usr/bin/python3
"""Python script that Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Function definition"""
    if list_of_integers:
        max_tmp = max_final = list_of_integers[0]
        length = len(list_of_integers) - 1
        j = 0
        for i in range(0, length // 2 + 1):
            j += 1
            max_tmp = list_of_integers[i] if (
                    list_of_integers[i] > list_of_integers[length - i]) else (
                            list_of_integers[length - i])
            max_final = max_tmp if max_tmp > max_final else max_final
        if len(list_of_integers) % 2 == 1:
            max_final = list_of_integers[i] if (
                    max_final < list_of_integers[i + 1]) else max_final
        return max_final
    else:
        return None
