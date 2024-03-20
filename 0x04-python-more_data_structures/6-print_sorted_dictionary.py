#!/usr/bin/python3
<<<<<<< HEAD
def print_sorted_dictionary(a_dictionary):
    for i in sorted(a_dictionary):
        print("{:s}: {}".format(i, a_dictionary[i]))
=======


def print_sorted_dictionary(a_dictionary):
    """
    A function that prints a dictionary by ordered keys
    """
    keys = list(a_dictionary.keys())
    keys.sort()
    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
