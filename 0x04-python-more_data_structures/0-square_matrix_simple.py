#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = matrix.copy()
    for x in range(len(new_m)):
        for y in range(len(new_m)):
            new_m[x][y] = new_m[x][y] ** 2
    return new_m
