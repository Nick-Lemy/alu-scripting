#!/usr/bin/python3
"""
Module
"""

import json
import requests
import sys


def top_ten(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'admin'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for i in response.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print(None)