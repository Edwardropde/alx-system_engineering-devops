#!/usr/bin/python3
"""
function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords
"""
import requests
import sys


def get_words(headers, data, subreddit, word_dic={}):
    if data:
        url = "https://www.reddit.com/r/{}/hot.json?after={}".format(
                subreddit, data)
    else:
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code > 300:
        return None
    listings = r.json()
    for listing in listings["data"]["children"]:
        words = listing["data"]["title"].split()
        for word in words:
            if word.lower() in word_dic.keys():
                word_dic[word.lower()] += 1
            else:
                word_dic[word.lower()] = 0
    if listings["data"]["after"] is not None:
        return get_words(headers, listings["data"]["after"],
                         subreddit, word_dic)
    else:
        return word_dic

def count_words(subreddit, word_list):
    headers = {
        'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                       'AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/76.0.3809.132 Safari/537.36')
    }
    words = get_words(headers, None, subreddit)
    if words is None:
        return None

    count_result = {}
    for word in word_list:
        count_result[word.lower()] = words.get(word.lower(), 0)

    count_result = {word: count for word, count in count_result.items() if count > 0}

    sorted_result = sorted(count_result.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_result:
        print("{}: {}".format(word, count))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
