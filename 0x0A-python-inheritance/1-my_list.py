#!/usr/bin/python3
"""
<<<<<<< HEAD
1-my_list module
=======
contains the MyList class
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
"""


class MyList(list):
<<<<<<< HEAD
    """
    MyList child of list
    """
    def print_sorted(self):
        """
        print_sorted - prints the list, but sorted
        """
=======
    """a subclass of list"""
    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        print(sorted(self))
