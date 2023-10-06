#!/usr/bin/python3
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
