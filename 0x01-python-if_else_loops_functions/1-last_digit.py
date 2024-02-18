#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
<<<<<<< HEAD
if number < 0:
    last_digit = ((number * -1) % 10) * -1
else:
    last_digit = number % 10
print(f"Last digit of {number:d} is {last_digit:d} and is", end=" ")
if last_digit > 5:
    print("greater than 5")
elif last_digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
=======
num = abs(number) % 10
if num > 5:
    print(f"Last digit of {number} is {num} and is greater than 5")
elif num == 0:
    print(f"Last digit of {number} is {num} and is 0")
elif num < 6 and num != 0:
    print(f"Last digit of {number} is {num} and is less than 6 and not 0")
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
