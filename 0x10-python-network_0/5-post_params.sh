#!/bin/bash
# post info using curl
curl -s -X  POST -d 'email: test@gamil.com' -d 'subject: I will always be here for PLD' "$1"
