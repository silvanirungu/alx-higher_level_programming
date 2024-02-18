#!/usr/bin/python3
<<<<<<< HEAD
"""
Defines Rectangle class
"""


class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """ initialize """
        self.width = width
        self.height = height

    def __str__(self):
        """ returns set of rectangle """
        if self.__height == 0 or self.__width == 0:
            return ''
        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += '#'
            ret += '\n'
        return ret[:-1]

    def __repr__(self):
        """ repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ del """
        print("Bye rectangle...")

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
        """Get/set the width of the Rectangle."""
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
        """Get/set the height of the Rectangle."""
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

    def area(self):
<<<<<<< HEAD
        """ calculates area of a rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of a rectangle """
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)
=======
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
