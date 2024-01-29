#!/bin/bash
# use curl
curl -s | sed '/HTTP/1.1 200/, $' | sed -n '/^$/.*'
