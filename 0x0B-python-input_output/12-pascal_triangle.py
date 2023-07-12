#!/usr/bin/python3
''' Module Pascal's Triangle
'''


def pascal_triangle(n):
    ''' Prints Pascal triangle
    '''
    matrix = []
    for i in range(n):
        s = str(11 ** i)
        matrix.append(list(c for c in s))
    return matrix
