#!/usr/bin/python3
<<<<<<< HEAD
"""script that takes in a URL,
sends a request to the URL and displays
the value of the X-Request-Id
"""
import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(dict(r.headers).get("X-Request-Id"))
=======
"""
get the x-request id
"""

import sys
import requests
if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers['X-Request-Id'])
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
