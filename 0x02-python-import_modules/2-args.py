#!/usr/bin/python3
<<<<<<< HEAD
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{} arguments.".format(num - 1))
    elif num == 2:
        print("{} argument:".format(num - 1))
    else:
        print("{} arguments:".format(num - 1))

    for i in range(1, num):
        print("{}: {}".format(i, sys.argv[i]))
=======
import sys
if __name__ == "__main__":
    length = len(sys.argv) - 1
    if length == 0:
        print("0 arguments.")
    elif length == 1:
        print("{} argument:".format(length))
        print("{}: {}".format(length, sys.argv[length]))
    elif length > 1:
        print("{} arguments:".format(length))
        arg_count = 1
        while arg_count <= length:
            print("{}: {}".format(arg_count, sys.argv[arg_count]))
            arg_count += 1
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
