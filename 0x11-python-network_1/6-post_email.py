#!/usr/bin/python3
<<<<<<< HEAD
"""script that takes in a URL and displays the body of the response 
(decoded in utf-8)
"""
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values = {"email": sys.argv[2]}

    request = requests.post(url, data=values)
    print(request.text)
=======
"""
post an email address
"""

import sys
import requests

if __name__ == "__main__":
    data = {
        'email' : sys.argv[2]
    }
    response = requests.post(sys.argv[1], data=data)
    print(response.text)
    
>>>>>>> f87d9a95787dde15a905f7ffe759820dd508082a
