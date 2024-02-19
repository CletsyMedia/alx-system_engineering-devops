import json
import requests


def export_all_tasks():
    url = 'https://jsonplaceholder.typicode.com/todos'
    response = requests.get(url)
    todos = response.json()

    all_tasks = {}

    for todo in todos:
        user_id = str(todo['userId'])

        if user_id not in all_tasks:
            all_tasks[user_id] = []

        task = {
            "username": todo['title'],
            "task": todo['title'],
            "completed": todo['completed']
        }

        all_tasks[user_id].append(task)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(all_tasks, json_file, indent=4)

    print("Data exported to todo_all_employees.json")


if __name__ == "__main__":
    export_all_tasks()
