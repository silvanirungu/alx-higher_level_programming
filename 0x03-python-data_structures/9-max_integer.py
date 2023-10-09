#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list[0] == None:
        return None
    else:
        x = len(my_list) - 1
        maxim = 0
        for y in range(x):
            if my_list[y] > maxim:
                maxim = my_list[y]
        return maxim
