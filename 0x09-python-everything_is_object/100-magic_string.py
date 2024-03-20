#!/usr/bin/python3
<<<<<<< HEAD
def magic_string(x=[]):
    x += ["BestSchool"]
    return (", ".join(x))
=======
def magic_string():
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return ("BestSchool, " * (magic_string.n - 1) + "BestSchool")
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
