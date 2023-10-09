#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = len(my_list) - 1
    for y in range(x):
        if my_list[y] % 2 == 0:
            my_list[y] = True
        else:
            my_list[y] = False
    return my_list
