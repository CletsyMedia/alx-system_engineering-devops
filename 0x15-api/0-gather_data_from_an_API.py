#!/usr/bin/python3
"""Retrieve employee information and TODO list from JSONPlaceholder API."""
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'

    user = '{}users/{}'.format(url, sys.argv[1])
    response = requests.get(user)
    json_o = response.json()
    print("Employee {} is done with tasks".format(json_o.get('name')), end="")

    todos = '{}todos?userId={}'.format(url, sys.argv[1])
    response = requests.get(todos)
    tasks = response.json()
    completed_task = []
    for task in tasks:
        if task.get('completed') is True:
            completed_task.append(task)

    print("({}/{}):".format(len(completed_task), len(tasks)))
    for task in completed_task:
        print("\t {}".format(task.get("title")))
