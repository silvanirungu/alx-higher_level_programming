#!/usr/bin/python3
<<<<<<< HEAD
def multiply_by_2(a_dictionary):
    new_d = {}
    for i in a_dictionary:
        new_d[i] = a_dictionary[i] * 2
    return new_d
=======


def multiply_by_2(a_dictionary):
    """
    A function that returns a new dictionary
    with all values multiplied by 2
    """
    new_dict = {}
    for key, value in a_dictionary.items():
        new_dict.update({key: (value * 2)})
    return new_dict
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
