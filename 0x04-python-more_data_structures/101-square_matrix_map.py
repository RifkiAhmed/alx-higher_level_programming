#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    matrix2 = []
    for row in matrix:
        matrix2 += [list(map(lambda x: x**2, row))]
    return matrix2
