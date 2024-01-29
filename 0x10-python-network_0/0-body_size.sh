#!/bin/bash
# prints the body size of the http response in bytes
curl -sI "$1" | grep -oP "Content-Length: \K.*"

