#!/usr/bin/python3
def uppercase(str):
<<<<<<< HEAD
    for c in str:
        if ord(c) <= ord('z') and ord(c) >= ord('a'):
            ch = chr(ord(c) - 32)
        else:
            ch = c
        print("{:s}".format(ch), end="")
    print('')
=======
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
