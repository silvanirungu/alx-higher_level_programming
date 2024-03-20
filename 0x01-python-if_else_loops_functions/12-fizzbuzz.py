#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
<<<<<<< HEAD
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
=======
        if i % 15 == 0:
            print("FizzBuzz ", end="")
        elif i % 5 == 0:
            print("Buzz ", end="")
        elif i % 3 == 0:
            print("Fizz ", end="")
        else:
            print("{:d} ".format(i), end="")
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
