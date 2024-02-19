#!/usr/bin/python3
"""
This script retrieves information about an employee's TODO list progress
from a given REST API.
"""

import requests
from sys import argv


def gather_employee_todo_progress(employee_id):
    """
    Retrieves information about an employee's TODO list progress
    Args:
        employee_id (int): The ID of the employee
    """

    # Base URL of the REST API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user info
    user_response = requests.get(base_url + "users/{}".format(employee_id))
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list
    todo_response = requests.get(base_url + "todos", params={"userId": employee_id})
    todo_data = todo_response.json()

    # Filter completed tasks
    completed_tasks = [task for task in todo_data if task.get("completed")]

    # Display progress
    total_tasks = len(todo_data)
    completed_count = len(completed_tasks)

    print(
        "Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_count, total_tasks
        )
    )

    for task in completed_tasks:
        print("\t{}".format(task.get("title")))


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: {} <employee_id>".format(argv[0]))
        exit(1)

    try:
        employee_id = int(argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        exit(1)

    gather_employee_todo_progress(employee_id)
