#!/usr/bin/python3
def print_list_integer(my_list=[]):
    x = len(my_list)
    for a in range(x):
        print("{:d}".format(my_list[a]))
