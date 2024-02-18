#!/usr/bin/python3
<<<<<<< HEAD
"""
module add_integer
a and b arguments
returns sum of a and b
"""


def add_integer(a, b=98):
    """
    add_integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')

=======
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
    return (int(a) + int(b))
