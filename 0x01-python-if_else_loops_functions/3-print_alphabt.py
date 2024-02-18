#!/usr/bin/python3
<<<<<<< HEAD
for c in range(ord('a'), ord('z') + 1):
    if c != ord('e') and c != ord('q'):
        print("{:c}".format(c), end="")
=======
for i in range(ord('a'), ord('z') + 1):
    if i == ord('e') or i == ord('q'):
        continue
    print("{:s}".format(chr(i)), end="")
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
