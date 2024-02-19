#!/usr/bin/python3
"""Retrieve employee information and TODO list from JSONPlaceholder API."""
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user_id = sys.argv[1]
    user_url = '{}users/{}'.format(url, user_id)
    response = requests.get(user_url)
    user_data = response.json()
    username = user_data.get('username')

    todos_url = '{}todos?userId={}'.format(url, user_id)
    response = requests.get(todos_url)
    todos_data = response.json()

    user_tasks = {user_id: []}
    for todo in todos_data:
        task_info = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': username
        }
        user_tasks[user_id].append(task_info)

    filename = '{}.json'.format(user_id)
    with open(filename, 'w') as json_file:
        json.dump(user_tasks, json_file)
