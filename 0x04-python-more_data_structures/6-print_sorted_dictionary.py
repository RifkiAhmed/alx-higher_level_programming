#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    for key in sorted(map(lambda key: key, a_dictionary)):
        print("{0}: {1}".format(key, a_dictionary[key]))
