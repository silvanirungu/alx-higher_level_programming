#!/usr/bin/python3
<<<<<<< HEAD
"""
Defines Rectangle class
"""


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initizie width and height """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width getter """
=======
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the rectangle."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        return self.__width

    @width.setter
    def width(self, value):
<<<<<<< HEAD
        """ width setter """
        if type(value) is not int:
=======
        if not isinstance(value, int):
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
<<<<<<< HEAD
        """ height getter """
=======
        """Get/set the height of the rectangle."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        return self.__height

    @height.setter
    def height(self, value):
<<<<<<< HEAD
        """ height setter """
        if type(value) is not int:
=======
        if not isinstance(value, int):
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
