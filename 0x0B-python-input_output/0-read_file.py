#!/usr/bin/python3
<<<<<<< HEAD
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of the file
    """
    with open(filename, "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
=======
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
