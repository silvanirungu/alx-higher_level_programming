#!/usr/bin/python3
def print_last_digit(number):
<<<<<<< HEAD
    if number < 0:
        number = -number
    last_digit = number % 10
    print(last_digit, end="")
    return last_digit
=======
    exe = 0
    if number < 0:
        number *= -1
    exe = 1
    last = number % 10
    if exe == 1:
        number *= -1
    print("{:d}".format(last), end="")
    return last
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
