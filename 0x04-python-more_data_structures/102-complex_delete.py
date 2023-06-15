#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for key in a_dictionary:
        if a_dictionary[key] == value:
            del (a_dictionary[key])
            complex_delete(a_dictionary, value)
            break
    return a_dictionary
