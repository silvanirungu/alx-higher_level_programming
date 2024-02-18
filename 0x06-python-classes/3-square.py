#!/usr/bin/python3
<<<<<<< HEAD
""" define a class Square """


class Square:
    """ define __init__ function """
    def __init__(self, size=0):
        """ if statement """
        if type(size) is not int:
            """ raise error """
            raise TypeError("size must be an integer")
        elif size < 0:
            """ raise error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize """
            self.__size = size
    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2
=======

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
