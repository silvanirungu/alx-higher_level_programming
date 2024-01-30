#!/usr/bin/python3
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
