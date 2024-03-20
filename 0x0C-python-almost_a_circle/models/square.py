#!/usr/bin/python3
<<<<<<< HEAD
"""
square module
"""
=======
'''Module for Square class.'''
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
from models.rectangle import Rectangle


class Square(Rectangle):
<<<<<<< HEAD
    """
    Square implementation
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init - initilizer
        Args:
            size: size of the square
            x: x position of the square
            y: y position of the square
            id: id of the square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        overriden __str__ method
        """
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        assigns attributes
        """
        lst = (self.id, self.size, self.x, self.y)
        if args:
            self.id, self.size, self.x, self.y = \
                    args + lst[len(args):len(lst)]
        elif kwargs:
            for (key, value) in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        that returns the dictionary representation of a Square.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
=======
    '''A Square class.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Constructor.'''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Returns string info about this square.'''
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        '''Size of this square.'''
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
