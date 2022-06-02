#!/usr/bin/python3
"""
that queries the Reddit API and
returns the number of subscribers
"""
import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/70.0.3538.77 Safari/537.36"}


def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    resp = requests.get(url, headers=header)
    if resp.status_code == 200:
        data = resp.json().get("data").get("subscribers")
        return(data)
    return (0)
