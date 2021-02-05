#!/usr/bin/python3
'''recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit. If no results are found
for the given subreddit, the function should return None.'''
import requests


def recurse(subreddit, hot_list=[], after='', count=0):
    '''Hint: The Reddit API uses pagination for
    separating pages of responses.'''
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'retr0-cc'
    }
    params = {
        'after': after,
        'count': count,
        'limit': 100
    }
    request = requests.get(url, headers=headers, params=params,
                           allow_redirects=False)
    if request.status_code == 404:
        return None
    articles = request.json().get('data')
    after = articles.get('after')
    count = articles.get('dist')
    for index in articles.get('children'):
        hot_list.append(index.get('data').get('title'))
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
