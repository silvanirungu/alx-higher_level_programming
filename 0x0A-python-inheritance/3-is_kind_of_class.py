#!/usr/bin/python3
<<<<<<< HEAD
"""
3-is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """
    is_kind_of_class: Check if an object is an instance,
                    or inherited instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns: If obj is an instance or inherited instance of a_class - True,
            Otherwise - False.
    """
    return isinstance(obj, a_class)
=======
"""Defines a class and inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an instance or inherited instance of a_class - True.
        Otherwise - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
