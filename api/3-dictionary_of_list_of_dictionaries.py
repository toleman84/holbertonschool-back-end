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

    user = request('users')
    out = {}
    for users in user:
        user_id = users['id']
        out.update({user_id: []})
        tasks = request('todos', ('userId', str(user_id)))
        for task in tasks:
            out[user_id].append({'username': users['username'],
                                 'task': task['title'],
                                 'completed': task['completed']})

    # Convert the data to JSON
    with open('todo_all_employees.json', mode='w') as file:
        json.dump(out, file)
