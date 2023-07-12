#!/usr/bin/python3
''' Module Pascal's Triangle
'''


def pascal_triangle(n):
    ''' Prints Pascal triangle
    '''
    if n < 0:
        return []
    my_matrix = []
    for i in range(1, n + 1):
        my_list = [1]
        for j in range(1, i):
            my_list.append(my_list[j - 1] * (i - j) // j)
        my_matrix.append(my_list)
    return my_matrix
