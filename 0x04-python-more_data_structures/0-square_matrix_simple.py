#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == [[]]:
        return None
    matrix2 = []
    for i in range(len(matrix)):
        matrix2 = matrix2 + [matrix[i][:]]
    for row in matrix2:
        for i in range(len(row)):
            row[i] = row[i] ** 2
    return matrix2
