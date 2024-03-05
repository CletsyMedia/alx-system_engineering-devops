#!/usr/bin/python3
"""
A recursive function that queries the Reddit API and returns a list containing
the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively fetches all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): List to store the titles of hot articles (default [])
        after (str): ID of the last post fetched, used for pagination (default None)

    Returns:
        list or None: List containing the titles of all hot articles for the given subreddit.
                      Returns None if the subreddit is invalid or if no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        for child in children:
            hot_list.append(child['data']['title'])
        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
