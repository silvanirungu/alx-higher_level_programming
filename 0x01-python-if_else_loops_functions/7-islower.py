#!/usr/bin/python3
def islower(c):
<<<<<<< HEAD
    if ord(c) <= ord("z") and ord(c) >= ord("a"):
        return True
    else:
        return False
=======
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    return False
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
