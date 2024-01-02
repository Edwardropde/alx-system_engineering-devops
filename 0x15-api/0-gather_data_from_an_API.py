#!/usr/bin/python3
"""Returns to-do list information of a particular employee"""
from sys import argv
import json
import requests


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the to-do list progress of a specific employee.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    try:
        url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        url_todo = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response_user = json.loads(requests.get(url_user).text)
        employee_name = response_user.get("name")

        response_todo = json.loads(requests.get(url_todo).text)

        total_tasks = len(response_todo)
        completed_tasks = sum(task["completed"] for task in response_todo)

        print(f'Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):')
        for task in response_todo:
            if task['completed']:
                print(f'\t{task["title"]}')

    except (ValueError, json.JSONDecodeError) as e:
        print(f"Error: {e}")
        exit(1)
    except requests.RequestException as e:
        print(f"Error: Unable to fetch data from the API. {e}")
        exit(1)


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script.py <employee_id>")
        exit(1)

    try:
        employee_id = int(argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        exit(1)
