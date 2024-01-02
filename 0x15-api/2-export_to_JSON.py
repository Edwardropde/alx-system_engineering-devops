#!/usr/bin/python3
"""Export to-do list information for a specific employee ID to JSON format"""
from urllib import request
import json
import requests
import sys


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    # Extract employee ID from command line argument
    u_id = sys.argv[1]

    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    try:
        # Fetch user information using the provided employee ID
        user_response = requests.get(url + "users/{}".format(u_id))

        # Check if the response status code is okay
        user_response.raise_for_status()

        # Parse user data from the JSON respons
        user_data = user_response.json()

        # Extract the username from user data
        username = user_data.get("username")

        # Fetch to-do list information for the specified user
        todos_response = requests.get(url + "todos", params={"userId": u_id})

        # Check if the response status code is okay
        todos_response.raise_for_status()

        # Parse to-do list data from the JSON response
        todos_data = todos_response.json()

        # Export to-do list information to a JSON file
        with open("{}.json".format(u_id), "w") as jsonfile:
            json.dump({u_id: [{"task": t.get("title"), "completed": t.get(
                "completed"), "username": username} for t in todos_data]}, jsonfile)

        print("Data exported to {}.json".format(u_id))

    except requests.RequestException as e:
        # Handle request-related exceptions
        print("Error: Unable to fetch data from the API. {}".format(e))
        sys.exit(1)
    except json.JSONDecodeError as e:
        # Handle JSON decoding exceptions
        print("Error: JSON decoding failed. {}".format(e))
        sys.exit(1)
