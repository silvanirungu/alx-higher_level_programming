#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
<<<<<<< HEAD
            else:
                result += a ** b / i
=======
            result += a ** b / i
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
        except Exception:
            result = b + a
            break
    return result
