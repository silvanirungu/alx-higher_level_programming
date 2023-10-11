#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    for x in matrix:
        result = list(map((lambda x: x**2), x))
        new_m.append(result)
    return new_m
