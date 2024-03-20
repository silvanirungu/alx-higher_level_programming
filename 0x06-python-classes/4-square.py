#!/usr/bin/python3
<<<<<<< HEAD
""" define a class Square """


class Square:
    """ define __init__ function """
    def __init__(self, size=0):
        """ initializes size of self with size """
=======

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        self.size = size

    @property
    def size(self):
<<<<<<< HEAD
        """ returns __size of self """
        return self.__size

    @size.setter
    def size(self, value):
        """ if statement """
        if type(value) is not int:
            """ raise error """
            raise TypeError("size must be an integer")
        elif value < 0:
            """ raise error """
            raise ValueError("size must be >= 0")
        else:
            """ initialize """
            self.__size = value
    """ defines area function """
    def area(self):
        """ returns area """
        return self.__size ** 2
=======
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
