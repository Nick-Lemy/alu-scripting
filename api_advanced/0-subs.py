#!/usr/bin/python3
"""
reddit api
"""
import requests


def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'My User Agent 1.0'}
    url = 'https://www.reddit.com/r/{}/about.json'
    response = requests.get(url.format(subreddit), headers=headers)
    data = response.json().get('data')
    if response.status_code == 200:      
        return data.get('subscribers')
    else:
        return 0
