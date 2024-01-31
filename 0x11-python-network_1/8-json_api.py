#!/usr/bin/python3
"""make a post request"""

import sys
import requests

if __name__ == "__main__":
    if (sys.argv[1] is not None):
        data = {
            'q' : sys.argv[1]
        }
    else:
        data = {
            'q' : ''
        }
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    if (response.headers['Content-Type'] is not 'application/json'):
        print('Not a valid JSON')
    elif (response.text is None):
        print('No result')
    else:
        print('[{}] {}'.format(response.text['id'],response.text['name']))
