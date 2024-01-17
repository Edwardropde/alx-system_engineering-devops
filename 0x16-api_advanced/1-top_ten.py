#!/usr/bin/python3
"""
function that queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit.
"""

import requests
import sys


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": 'Google Chrome Version 81.0.4044.129'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get("data", {})
        children = data.get("children", [])

        if not children:
            print("None")
            return

        for child in children:
            print(child.get("data", {}).get("title"))
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            print("None")
        else:
            print(f"Error: {e}")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
