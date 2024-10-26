#!/usr/bin/python3
"""
This module contains the function top_ten.
"""
import requests


def top_ten(subreddit):
    """
    Returns the top ten posts for a given subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'admin'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        for i in response.json().get("data").get("children"):
            print(i.get("data").get("title"))
    else:
        print(None)

if __name__ == "__main__":
    if len(argv) > 1:
        top_ten(argv[1])
    else:
        print("Usage: ./script.py <subreddit>")