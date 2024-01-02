#!/usr/bin/python3
"""Exports to-do list information for a specific emplotee ID to CSV format"""
from sys import argv
import csv
import json
import requests


def export_to_csv(employee_id):
    """
    Fetches and exports to-do list progress of specific employee to CSV file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    try:
        url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        url_todo = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
        response_user = json.loads(requests.get(url_user).text)
        response_todo = json.loads(requests.get(url_todo).text)

        tasks = response_todo.__len__()
        completed_tasks = [task for task in response_todo if task["completed"]]

        print(f'Employee {response_user.get("name")} is done with tasks({len(completed_tasks)}/{tasks}):')
        for task in completed_tasks:
            print(f"\t{task['title']}")
        with open(f"{employee_id}.csv", mode="w", newline='') as to_csv:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.writer(to_csv, delimiter=",", quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
            writer.writerow(fieldnames)
            for task in response_todo:
                writer.writerow({
                    response_user.get("id"),
                    response_user.get("username"),
                    str(task["completed"]),
                    task["title"]
                })
        print(f'Data exported to {employee_id}.csv')
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
        export_to_csv(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        exit(1)
