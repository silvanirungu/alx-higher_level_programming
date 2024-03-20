#!/bin/bash
<<<<<<< HEAD
#script that takes in a URL and sends a POST request to the passed URL
curl -s -X "POST" -d "email=test@gmail.com&subject=I will always be here for PLD" $1
=======
# post info using curl
curl -s -X  POST -d 'email=test@gmail.com&subject=I will always be here for PLD' "$1"
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
