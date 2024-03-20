#!/usr/bin/python3
<<<<<<< HEAD
def update_dictionary(a_dictionary, key, value):
    if key not in a_dictionary:
        a_dictionary[key] = value
    else:
        for i in a_dictionary:
            if i == key:
                a_dictionary[i] = value
=======


def update_dictionary(a_dictionary, key, value):
    """
    A function that replaces or adds
    key/value in a dictionary.
    """
    a_dictionary[key] = value
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
    return a_dictionary
