#!/usr/bin/python3
'''function that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit.'''
import requests


def top_ten(subreddit):
    '''function that queries the Reddit API'''
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        'User-Agent': 'retr0-cc'
    }
    request = requests.get(url, headers=headers, allow_redirects=False)
    if request.status_code == 404:
        print('None')
        return
    titles = request.json().get('data')
    for index in titles.get('children'):
        print(index.get('data').get('title'))
