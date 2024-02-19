#!/usr/bin/python3
""" Script that exports data to CSV format """
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user_id = sys.argv[1]

    # Fetch user details
    user_response = requests.get(f"{url}users/{user_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch tasks
    tasks_response = requests.get(f"{url}todos?userId={user_id}")
    tasks = tasks_response.json()

    # Prepare CSV file name
    csv_filename = f"{user_id}.csv"

    # Write tasks to CSV file
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in tasks:
            task_completed_status = "True" if task.get(
                "completed") else "False"
            task_title = task.get("title")
            csv_writer.writerow(
                [user_id, username, task_completed_status, task_title])

    print(f"Data exported to {csv_filename} successfully.")
