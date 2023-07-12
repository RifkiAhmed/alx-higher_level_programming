#!/usr/bin/python3
''' Module Pascal's Triangle
'''


def pascal_triangle(n):
    ''' Prints Pascal triangle
    '''
    if n <= 0 or type(n) is not int:
        return []
    elif type(n) is int:
        m = []
        for i in range(n):
            m.append(list(int(c) for c in str(11 ** i)))
        return m
