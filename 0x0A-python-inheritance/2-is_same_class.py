#!/usr/bin/python3
<<<<<<< HEAD
"""
2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
    is_same_class - check if an object is exactly an instance of a given class.
    Args:
        ibj: The object to check.
        a_class: The class to match the type of obj to.
    Returns: If obj is exactly an instance of a_class - True,
            Otherwise - False.
    """
    return True if type(obj) is a_class else False
=======
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
