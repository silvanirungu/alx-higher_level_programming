#!/usr/bin/python3
<<<<<<< HEAD
def uniq_add(my_list=[]):
    new_list = set(my_list)
    result = 0
    for i in new_list:
        result += i
    return result
=======


def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    new_list = []
    sum = 0
    for num in my_list:
        if num not in new_list:
            sum += num
            new_list.append(num)
    return sum
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
