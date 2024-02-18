#!/usr/bin/python3
<<<<<<< HEAD
"""script that takes in a URL and displays the body of the response 
(decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode("ascii")
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
=======
"""
send a post request in a url
"""

import sys
import urllib.request
import urllib.parse
if __name__ == "__main__" :
    data = {
        'email': sys.argv[2]
    }
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    url = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print(body.decode('utf-8'))
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
