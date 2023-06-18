#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    first_key = list(a_dictionary)[0]
    key_name = ""
    for key in a_dictionary:
        if a_dictionary[first_key] < a_dictionary[key]:
            a_dictionary[first_key] = a_dictionary[key]
            key_name = key
    return key_name
