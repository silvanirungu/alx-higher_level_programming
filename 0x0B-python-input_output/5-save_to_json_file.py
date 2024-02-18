#!/usr/bin/python3
<<<<<<< HEAD
"""
5-save_to_json module
"""
=======
"""Defines a JSON file-writing function."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
import json


def save_to_json_file(my_obj, filename):
<<<<<<< HEAD
    """
    save_to_json_file -  writes an Object to a text file,
                        using a JSON representation:
    Args:
        my_obj:
        filename:
    Return:
    """
=======
    """Write an object to a text file using JSON representation."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
    with open(filename, "w") as f:
        json.dump(my_obj, f)
