#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import csv
import requests
import sys


if __name__ == "__main__":
    base_url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user_url = '{}users/{}'.format(base_url, user_id)
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username')

    todos_url = '{}todos?userId={}'.format(base_url, user_id)
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    tasks = []
    for todo in todos_data:
        tasks.append([user_id,
                      username,
                      todo.get('completed'),
                      todo.get('title')])

    filename = '{}.csv'.format(user_id)
    with open(filename, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file,
                                delimiter=',',
                                quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for task in tasks:
            csv_writer.writerow(task)
