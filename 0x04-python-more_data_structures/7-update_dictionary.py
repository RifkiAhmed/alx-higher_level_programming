#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for my_key in a_dictionary:
        if my_key == key:
            a_dictionary[my_key] = value
            return a_dictionary
    a_dictionary[key] = value
    return a_dictionary
