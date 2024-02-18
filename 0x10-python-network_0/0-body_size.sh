#!/bin/bash
<<<<<<< HEAD
#bash script for displaying length
curl -sI "$1" | grep "Content-Length:" | cut -d " " -f 2
=======
# prints the body size of the http response in bytes
curl -sI "$1" | grep -oP "Content-Length: \K.*"
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
