#!/usr/bin/python3
<<<<<<< HEAD
"""
append_write module
"""


def append_write(filename="", text=""):
    """
    write_file - appends a string at the end of a text file (UTF8),
                and returns the number of characters added:
    Args:
        filename: name of the file
        text: text to be written
    Return: number of bytes written.
    """
    with open(filename, mode="a", encoding="UTF-8") as f:
        return (f.write(text))
=======
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Appends a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
