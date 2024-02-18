#!/bin/bash
<<<<<<< HEAD
#script that takes in a URL and displays all HTTP methods
=======
# show methods
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
