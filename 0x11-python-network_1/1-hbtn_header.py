#!/usr/bin/python3
<<<<<<< HEAD
"""script that takes in a URL and sends a request to the URL and displays"""
import urllib.request
import sys

if __name__ == '__main__':
    with urllib.request.urlopen(sys.argv[1]) \
            as response:
        print(dict(response.headers).get("X-Request-Id"))
=======
"""
get the request id
"""

import sys
import urllib.request
if __name__ == "__main__":
    url = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print('{}'.format(response.headers.get('X-Request-Id')))
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
