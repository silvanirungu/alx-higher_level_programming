#!/usr/bin/python3
<<<<<<< HEAD
"""
10-square module
"""
=======
"""Defines a Rectangle subclass Square."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
<<<<<<< HEAD
    """
    Represents a square.
    Inherits from Rectangle.
    """
    def __init__(self, size):
        """
        init - Initializes a Square.
        Args:
            size: size of the square
=======
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
<<<<<<< HEAD

    def area(self):
        """
        area - returns area of a square
        """
        return self.__size ** 2
=======
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
