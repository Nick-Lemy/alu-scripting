#!/usr/bin/python3


"""
reddit api
"""


import requests


def number_of_subscribers(subreddit):
    url = 'https://www.reddit.com/r/{}/about.json'
    response = requests.get(url.format(subreddit))
    data = response.json()
    if response.status_code != 200:
        return 0
    else:
        return data['data']['subscribers']
