#!/usr/bin/python3
"""doc"""

import csv
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

    csv_file = sys.argv[1] + '.csv'
    # Open a CSV file for writing
    with open(csv_file, mode='w') as file:
        # Write the data to the CSV file
        writer = csv.writer(file,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        # "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
        for task in tasks:
            writer.writerow([user['id'],
                             user['username'],
                             task['completed'],
                             task['title']])
