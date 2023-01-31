#!/usr/bin/python3
"""
This module queries the Reddit API and returns the number of
subscribers (not active users, total subscribers) for a given subreddit.
If an invalid subreddit is given, the function should return 0
"""

import requests
import sys
import json


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'kia1234'}
    r = requests.get(url, headers=header, allow_redirects=False)
    if r.status_code == 200:
        return (r.json()['data']['subscribers'])
    else:
        return (0)
