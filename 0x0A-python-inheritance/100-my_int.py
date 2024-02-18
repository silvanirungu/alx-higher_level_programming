#!/usr/bin/python3
<<<<<<< HEAD
"""
100-my_int module
"""


class MyInt(int):
    """
    Class inheriting from int,
    But reverses the behavior of != and ==.
    """
    def __eq__(self, other):
        """
        Equality becomes inequality.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inequality becomes equality.
        """
        return super().__eq__(other)
=======
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator with == behavior."""
        return self.real == value
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
