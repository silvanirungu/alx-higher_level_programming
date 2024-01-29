#!/bin/bash
# send info in a get request
curl -s --request GET "$1"'?X-School-User-Id=98'
