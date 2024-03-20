#!/usr/bin/python3
<<<<<<< HEAD
"""
4-from_json_string module
"""
=======
# 6-from_json_string.py
"""Defines a JSON-to-object function."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
import json


def from_json_string(my_str):
<<<<<<< HEAD
    """
    from_json_string - returns an object (Python data structure)
                    represented by a JSON string:
    Args:
        my_str: json string to represent
    Return: object
    """
=======
    """Return the Python object representation of a JSON string."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
    return json.loads(my_str)
