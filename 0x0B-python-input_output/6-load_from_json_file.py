#!/usr/bin/python3
<<<<<<< HEAD
"""
6-load_from_json_file module
"""
=======
"""Defines a JSON file-reading function."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
import json


def load_from_json_file(filename):
<<<<<<< HEAD
    """
    load_from_json_file - loads an object from JSON file.
    Args:
        filename: name of the file
    """
    with open(filename, "r") as f:
        my_obj = json.load(f)
        return my_obj
=======
    """Create a Python object from a JSON file."""
    with open(filename) as f:
        return json.load(f)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
