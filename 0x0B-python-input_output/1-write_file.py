#!/usr/bin/python3
<<<<<<< HEAD
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    write_file - writes a string to a text file (UTF8),
                and returns the number of characters written:
    Args:
        filename: name of the file
        text: text to be written
    Return: number of bytes written.
    """
    with open(filename, mode="w", encoding="UTF-8") as f:
        return (f.write(text))
=======
"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
