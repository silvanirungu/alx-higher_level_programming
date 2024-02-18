#!/usr/bin/python3
<<<<<<< HEAD
def best_score(a_dictionary):
    if a_dictionary and len(a_dictionary):
        max = list(a_dictionary.keys())[0]
        for key in a_dictionary:
            if a_dictionary[key] > a_dictionary[max]:
                max = key
        return max
    return None
=======


def best_score(a_dictionary):
    """
    A function that returns a key with the biggest integer value.
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        leader = ""
        for i in my_list:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                leader = i
        return leader
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
