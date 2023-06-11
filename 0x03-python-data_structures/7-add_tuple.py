#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_list = list(tuple_a)
    b_list = list(tuple_b)
    c_list = []
    for i in range(2):
        a_list.append(0)
        b_list.append(0)
        c_list.append(a_list[i] + b_list[i])
    return (c_list[0], c_list[1])
