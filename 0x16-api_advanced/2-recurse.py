#!/usr/bin/python3
"""
recursive function that queries the Reddit API
and returns a list containing the titles
of all hot articles for a given subreddit
"""
import requests

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
          AppleWebKit/537.36 (KHTML, like Gecko) \
          Chrome/70.0.3538.77 Safari/537.36"}


def recurse(subreddit, hot_list=[], after=""):
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    resp = requests.get(url, headers=header, params={'after': after})

    if after is None:
        return hot_list

    if resp.status_code == 200:
        resp = resp.json()
        after = resp.get("data").get("after")
        hots = resp.get("data").get("children")
        for element in hots:
            hot_list.append(element.get("data").get("title"))
        return recurse(subreddit, hot_list, after)
    return None
