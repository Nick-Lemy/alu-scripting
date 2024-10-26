#!/usr/bin/python3


"""
reddit api
"""

import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'
    response = requests.get(url.format(subreddit), headers=headers)
    data = response.json()
    if response.status_code != 200:
        return 0
    else:
        return data['data']['subscribers']
