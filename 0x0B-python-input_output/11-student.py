#!/usr/bin/python3
<<<<<<< HEAD
'''Module for Student class.'''


class Student:
    '''Class for jsonification.'''
    def __init__(self, first_name, last_name, age):
        '''Constructor.'''
=======
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
<<<<<<< HEAD
        '''Retrieves dictionary with filter.'''
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        '''Loads attributes from json.'''
        for key, value in json.items():
            self.__dict__[key] = value
=======
        """Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.

        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
