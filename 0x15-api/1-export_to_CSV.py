#!/usr/bin/python3
"""Exports to-do list information for a specific emplotee ID to CSV format"""
import csv
import requests
import sys

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users/' + sys.argv[1]
    r = requests.get(url)
    if r.status_code == 200:
        username = r.json().get("username")
        url2 = 'https://jsonplaceholder.typicode.com/todos'
        r2 = requests.get(url2)
        filename = sys.argv[1] + '.csv'
        with open(filename, 'w') as f:
            wr = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
            for item in r2.json():
                if item.get("userId") == int(sys.argv[1]):
                    line = [item.get("userId"),
                            username,
                            str(item.get("completed")),
                            item.get('title')]
                    wr.writerow(line)
