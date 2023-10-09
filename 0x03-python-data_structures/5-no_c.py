#!/usr/bin/python3
def no_c(my_string):
    newstr = ''
    for x in range(len(my_string) - 1):
        if my_string[x] != 'c' and my_string[x] != 'C':
            newstr += my_string[x]
    return newstr
