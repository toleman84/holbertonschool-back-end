#!/usr/bin/python3
"""doc"""

import sys
import requests


if __name__ == '__main__':
    """code should not be executed when imported"""

    def request(resource, parameter=None):
        """API data"""
        url = 'https://jsonplaceholder.typicode.com/'
        url += resource
        if parameter:
            url += ('?' + parameter[0] + '=' + parameter[1])
        request = requests.get(url)
        request = request.json()
        return request
