#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
<<<<<<< HEAD
    for i in range(len(my_list)):
        if my_list[i] == search:
            new_list.append(replace)
        else:
            new_list.append(my_list[i])
=======
    for element in my_list:
        if element == search:
            new_list.append(replace)
        else:
            new_list.append(element)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
    return new_list
