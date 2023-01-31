#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot
posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """ top ten posts """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-Agent': 'kia1234'}
    p = {'limit': 10}
    r = requests.get(url, headers=h, params=p, allow_redirects=False)

    if r.status_code == 200:
        titles = r.json().get('data').get('children')
        for title in titles:
            print(title.get('data').get('title'))
    else:
        print(None)
