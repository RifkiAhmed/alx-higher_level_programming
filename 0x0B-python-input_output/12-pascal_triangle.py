#!/usr/bin/python3
''' Module Pascal's Triangle
'''


def pascal_triangle(n):
    ''' Prints Pascal triangle
    '''
    if n <= 0:
        return []
    m = []
    for i in range(n):
        s = str(11 ** i)
        m.append(list(int(c) for c in s))
    return m
