#!/usr/bin/python3
<<<<<<< HEAD
"""script that takes in a URL and displays the body of the response 
(decoded in utf-8)
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]

    request = requests.get(url)
    if request.status_code >= 400:
        print(f"Error code: {request.status_code}")
    else:
        print(request.text)
=======
""" handle errors"""

import sys
import requests

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if (response.status_code >= 400):
        print('Error code: {}'.format(response.status_code))
    else:
        print(response.text)
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
