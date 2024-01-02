#!/usr/bin/python3
"""Exports to-do list information for a specific emplotee ID to CSV format"""
import csv
import requests
import json
from sys import argv


if __name__ == "__main__":
    url1 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    url2 = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    response1 = json.loads(requests.get(url1).text)
    response2 = json.loads(requests.get(url2).text)
    tasks = response2.__len__()
    tc_list = []
    for i in range(tasks):
        if response2[i]["completed"]:
            tc_list.append(i)
    print("Employee {} is done with tasks({}/{}):".format(
        response1.get("name"), len(tc_list), tasks))
    for i in range(len(tc_list)):
        print(f"\t {response2[tc_list[i]]['title']}")
    with open(f"{argv[1]}.csv", mode="w") as to_csv:
        writer = csv.writer(to_csv, delimiter=",", quotechar='"',
                            quoting=csv.QUOTE_ALL)
        for i in range(tasks):
            writer.writerow([response1.get("id"), response1.get("username"),
                            response2[i]["completed"], response2[i]["title"]])
