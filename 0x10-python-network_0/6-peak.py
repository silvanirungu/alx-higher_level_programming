#!/usr/bin/python3
<<<<<<< HEAD
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
=======
""" finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
    Args:
        list_of_integers(int): list of integers to find peak of
    Returns: peak of list_of_integers or None
    """
    list = list_of_integers
    peak = None
    x = len(list)
    index = 0
    condition = True
    while (index < x):
        if (condition):
            if (list[0] > list[index + 1]):
                peak = list[index]
                condition = False
                continue
        index += 1
        if (list[index] > list[index - 1] and list[index] > list[index + 1]):
            peak = list[index]
            return peak
        if (index == x - 1):
            if (peak is not None):
                return peak
            elif (list[index] > list[index - 1]):
                peak = list[index]
                return peak
            else:
                return None
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
