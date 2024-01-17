#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit. If an invalid
subreddit is given, the function should return 0.

Hint: No authentication is necessary for most features of the Reddit API.
If you’re getting errors related to Too Many Requests, ensure you’re
setting a custom User-Agent.
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    returns the number of subscribers
    If not a valid subreddit, return 0.
    """
    # Check if the subredit is none, Return 0
    if subreddit is None or subreddit is not isinstance(subreddit, str):
        return 0

    # Identifiying the user agent
    userAgent = {' User-agent': 'Google Chrome Version 81.0.4044.129'}

    # Identify the url
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    # Make the requesst
    response = get(url, head=userAgent)

    # Convert the response intp json format
    jsonResponse = response.json()

    # Try to get the number of subscribes
    try:
        return jsonResponse.get('data').get('subscribers')
    # If you could't get it
    except exceptions.RequestException as e:
        return 0
