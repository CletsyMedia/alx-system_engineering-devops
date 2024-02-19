#!/usr/bin/python3
"""Retrieve employee information and TODO list from JSONPlaceholder API."""

import requests
import sys


def get_employee_info(employee_id):
    """Retrieve employee information."""
    url = "https://jsonplaceholder.typicode.com/"
    user_url = f"{url}users/{employee_id}"
    response = requests.get(user_url)
    if response.status_code != 200:
        print(
            f"Error: Failed to retrieve employee information. "
            f"Status code: {response.status_code}"
        )
        sys.exit(1)
    return response.json()


def get_completed_tasks(employee_id):
    """Retrieve completed tasks for the employee."""
    url = "https://jsonplaceholder.typicode.com/"
    todos_url = f"{url}todos?userId={employee_id}"
    response = requests.get(todos_url)
    if response.status_code != 200:
        print(
            f"Error: Failed to retrieve employee's tasks. "
            f"Status code: {response.status_code}"
        )
        sys.exit(1)
    return [task["title"] for task in response.json() if task["completed"]]


def print_employee_progress(employee_name, completed_tasks, total_tasks):
    """Print employee progress."""
    print(
        f"Employee {employee_name} is done with tasks "
        f"({len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t{task}")


if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_info = get_employee_info(employee_id)
    employee_name = employee_info.get("name")
    total_tasks = len(employee_info.get("todos", []))
    completed_tasks = get_completed_tasks(employee_id)

    print_employee_progress(employee_name, completed_tasks, total_tasks)
