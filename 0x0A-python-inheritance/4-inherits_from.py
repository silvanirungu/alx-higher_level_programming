#!/usr/bin/python3
<<<<<<< HEAD
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    inherits_from - Checks if an object is an inherited instance of a class.
    Args:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    Returns: If obj is an inherited instance of a_class - True,
            Otherwise - False.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
=======
"""Defines an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is an inherited instance of a_class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
