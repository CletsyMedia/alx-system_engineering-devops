#!/usr/bin/python3
""" Script that uses JSONPlaceholder API to get information about employee """
import json
import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    users_endpoint = "{}users".format(api_url)
    users_response = requests.get(users_endpoint)
    users_data = users_response.json()
    tasks_dict = {}

    for user_data in users_data:
        username = user_data.get("username")
        user_id = user_data.get("id")
        todos_endpoint = "{}todos?userId={}".format(api_url, user_id)
        todos_response = requests.get(todos_endpoint)
        todos_data = todos_response.json()
        user_tasks = []

        for task_data in todos_data:
            task_dict = {
                "username": username,
                "task": task_data.get("title"),
                "completed": task_data.get("completed"),
            }
            user_tasks.append(task_dict)

        tasks_dict[str(user_id)] = user_tasks

    output_filename = "todo_all_employees.json"
    with open(output_filename, mode="w") as output_file:
        json.dump(tasks_dict, output_file)
