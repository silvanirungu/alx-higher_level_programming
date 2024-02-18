#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
<<<<<<< HEAD
str = str[39:66] + str[106:112] + str[:6]
=======
str = str[39:66] + str[6] + str[107:111] + str[6] + str[0:6]
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
print(str)
