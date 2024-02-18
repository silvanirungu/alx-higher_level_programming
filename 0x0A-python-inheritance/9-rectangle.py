#!/usr/bin/python3
<<<<<<< HEAD
"""
9-rectangle module
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
        init - Initializes an instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        area - returns area
        """
        return self.__width * self.__height

    def __str__(self):
        """
        str - returns rectangle description
        """
        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
=======
    """Represent a rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
