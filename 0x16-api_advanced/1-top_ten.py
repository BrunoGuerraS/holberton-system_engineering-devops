#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests


entitie = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/70.0.3538.77 Safari/537.36"}


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    resp = requests.get(url, headers=entitie)
    if resp.status_code == 200:
        data = resp.json().get("data")
        children = data.get("children")
        for child in children:
            print(child.get("data").get("title"))
    else:
        print(None)
