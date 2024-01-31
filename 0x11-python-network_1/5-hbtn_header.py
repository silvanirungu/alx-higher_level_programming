#!/usr/bin/python3
"""
get the x-request id
"""

import sys
import requests
if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
