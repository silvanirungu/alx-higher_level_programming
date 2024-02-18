#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
<<<<<<< HEAD
    new_matrix = [[x ** 2 for x in row] for row in matrix]
    return new_matrix
=======
    new_m = []
    for x in matrix:
        result = list(map((lambda x: x**2), x))
        new_m.append(result)
    return new_m
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
