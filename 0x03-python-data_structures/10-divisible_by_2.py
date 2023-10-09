#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = len(my_list) - 1
    copy = my_list.copy()
    for y in range(x):
        if my_list[y] % 2 == 0:
            copy[y] = True
        else:
            copy[y] = False
    return copy
