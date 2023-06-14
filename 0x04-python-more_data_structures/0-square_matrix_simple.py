#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == [[]]:
        return [[]]
    for row in matrix:
        for i in range(len(row)):
            row[i] = row[i] ** 2
    return matrix
