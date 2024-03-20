#!/usr/bin/python3
<<<<<<< HEAD
"""
7-base_geometry module
"""


class BaseGeometry:
    """
    Reprsent base geometry.
    """
    def area(self):
        """
        Not yet implemented.
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Args:
            name: The name of the parameter.
            value: The parameter to validate.
=======
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsent base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
<<<<<<< HEAD
        if type(value) is not int:
=======
        if type(value) != int:
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
