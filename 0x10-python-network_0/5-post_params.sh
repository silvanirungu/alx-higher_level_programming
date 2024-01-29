#!/bin/bash
# post info using curl
curl -s -X  POST -d 'email=test@gamil.com&subject=I will always be here for PLD' "$1"
