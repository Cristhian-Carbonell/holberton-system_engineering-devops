#!/usr/bin/python3
'''Function that queries the Reddit API and returns the number
of subscriber (not active users, total subscribers for a given
sybreddit. If an invalid subreddit is given, the function should
return 0)'''
import requests


def number_of_subscribers(subreddit):
    '''Function that queries the Reddit API'''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        'User-Agent': 'retr0-cc'
    }
    request = requests.get(url, headers=headers, allow_redirects=False)
    if request.status_code == 404:
        return 0
    no_subscribres = request.json().get('data').get('subscribers')
    return no_subscribres
