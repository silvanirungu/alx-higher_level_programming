#!/usr/bin/python3
<<<<<<< HEAD
"""
    Module for class Student.
"""


class Student:
    """
        A class students that defines a student by:
        Attributes:
            first_name (str): name of student.
            last_name (str): name of student.
            age (int): age of student.
        Methods:
            __init__ - initializes the Student instance.
            to_json - retrieves dictionary repr of Student instance.
    """
    def __init__(self, first_name, last_name, age):
        """
            Initialises Student instance.
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
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
<<<<<<< HEAD
        """
            retrieves a dictionary representation of Student.
        """
=======
        """Get a dictionary representation of the Student."""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        return self.__dict__
