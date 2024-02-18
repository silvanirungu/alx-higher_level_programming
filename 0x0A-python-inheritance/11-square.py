#!/usr/bin/python3
"""
<<<<<<< HEAD
10-square module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Inherits from Rectangle.
    """
    def __init__(self, size):
        """
        init - Initializes a Square.
        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area - returns area of a square
        """
        return self.__size ** 2

    def __str__(self):
        """
        str - returns square description
        """
        return str("[Square] {}/{}".format(self.__size, self.__size))
=======
more class base
"""


Rectangle = __import__('9-rectangle').Rectangle


"""
Square class
"""


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size):
        """ size init"""
        self.__size = size
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
