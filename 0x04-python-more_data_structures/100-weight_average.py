#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
<<<<<<< HEAD
    average = 0
    div = 0
    for tup in my_list:
        average += tup[0] * tup[1]
        div += tup[1]
    return float(average / div)
=======

    num = 0
    den = 0

    for tup in my_list:
        num += tup[0] * tup[1]
        den += tup[1]

    return (num / den)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
