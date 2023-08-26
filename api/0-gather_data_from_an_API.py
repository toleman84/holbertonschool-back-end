#!/usr/bin/python3
"""doc"""

from sys import argv
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

    user = request('users', ('id', argv[1]))
    tasks = request('todos', ('userId', argv[1]))
    done_tasks = [task for task in tasks if task['completed']]

    print('Employee {} is done with tasks({}/{}):'.format(user[0]['name'],
                                                          len(done_tasks),
                                                          len(tasks)))

    for task in done_tasks:
        print('\t {}'.format(task['title']))
