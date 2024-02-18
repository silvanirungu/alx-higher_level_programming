#!/usr/bin/python3
<<<<<<< HEAD
""" declares a class called MagicClass """
=======

>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
import math


class MagicClass:
<<<<<<< HEAD
    """ declaration of __init__ function """
    def __init__(self, radius=0):
        """ initialization of _MagicClass__radius with 0 """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius
    """ defines a function named area """
    def area(self):
        """ returns area """
        return self._MagicClass__radius ** 2 * math.pi
    """ defines a function named circumference """
    def circumference(self):
        """ returns circumference """
        return 2 * math.pi * self._MagicClass__radius
=======
    """Represent a circle."""

    def __init__(self, radius=0):
        """Initialize a MagicClass.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
