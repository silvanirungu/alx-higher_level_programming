#!/bin/bash
<<<<<<< HEAD
#script that takes in a URL as an argument, sends a GET request to the URL
curl -s "$1" -X GET -H "X-School-User-Id: 98"
=======
# send info in a get request
curl -sH 'X-School-User-Id:98' "$1"
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
