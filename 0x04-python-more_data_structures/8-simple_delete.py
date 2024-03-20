#!/usr/bin/python3
<<<<<<< HEAD
def simple_delete(a_dictionary, key=""):
=======


def simple_delete(a_dictionary, key=""):
    """
    A function that deletes a key in a dictionary.
    """
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
