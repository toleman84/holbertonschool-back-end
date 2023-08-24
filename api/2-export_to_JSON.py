#!/usr/bin/python3
"""doc"""

import json
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

    user = request('users', ('id', sys.argv[1]))[0]
    tasks = request('todos', ('userId', sys.argv[1]))

    user_id = user['id']
    out = {user_id: []}
    for task in tasks:
        out[user_id].append({'task': task['title'],
                             'completed': task['completed'],
                             'username': user['username']})

    # Convert the data to JSON
    with open(sys.argv[1] + '.json', mode='w') as file:
        json.dump(out, file)
