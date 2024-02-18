#!/usr/bin/python3
<<<<<<< HEAD
"""
LockedClass class
"""


class LockedClass:
    """ setattr """
=======
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
    __slots__ = ["first_name"]
