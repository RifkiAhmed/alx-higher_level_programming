#!/usr/bin/python3
def no_c(my_string):
    if my_string != "":
        new_string = ""
        for c in my_string:
            if c in ["c", "C"]:
                continue
            else:
                new_string += c
        return new_string
