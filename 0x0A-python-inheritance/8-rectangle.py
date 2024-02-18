#!/usr/bin/python3
<<<<<<< HEAD
"""
8-rectangle module
"""
=======
"""Defines a class Rectangle that inherits from BaseGeometry."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
<<<<<<< HEAD
    """
    Represents a rectangle.
    Inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes an instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
=======
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        self.__height = height
