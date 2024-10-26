#!/usr/bin/python3

import requests
def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'
    data = requests.get(url.format(subreddit), headers=headers).json()
    try:
        return data["data"]['subscribers']
    except:
        return 0