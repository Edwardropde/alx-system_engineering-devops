#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re
setting a custom User-Agent.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    If not a valid subreddit, return 0.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": 'Google Chrome Version 81.0.4044.129'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json().get("data", {})
        subscribers = data.get("subscribers", 0)
        return subscribers
    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:  # Not Found
            return 0
        else:
            print(f"Error: {e}")
            return 0
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit_name = sys.argv[1]
        subscribers = number_of_subscribers(subreddit_name)
        print("{:d}".format(subscribers))
