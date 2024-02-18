#!/bin/bash
<<<<<<< HEAD
#Script for displaying body of the response
curl -sL $1
=======
# use curl
[ $(curl -s -o /dev/null -w "%{http_code}" $1) -eq 200 ] && curl -s $1
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
