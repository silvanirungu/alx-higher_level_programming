#!/bin/bash
# use curl
curl -sI "$1" | grep -oP "^$\K.*"
