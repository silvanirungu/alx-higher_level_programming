#!/usr/bin/python3
<<<<<<< HEAD
for i in range(9):
    for j in range(i + 1, 10):
        if i == 8:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
=======
for i in range(0, 9):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{:d}{:d}".format(i, j))
        else:
            print("{:d}{:d}".format(i, j), end=", ")
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
