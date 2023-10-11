#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    square = lambda x : x**2
    for x in matrix:
        result = list(map(square, x))
        new_m.append(result)
    return new_m
