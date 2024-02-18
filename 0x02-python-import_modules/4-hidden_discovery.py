#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    from hidden_4 import *
    arr = dir()
    for i in range(0, len(arr)):
        if arr[i][0:2] != "__":
            print("{}".format(arr[i]))
=======

if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
