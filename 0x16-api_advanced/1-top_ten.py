#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Custom User Agent'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        if children:
            for i, child in enumerate(children, 1):
                if not child['data']['stickied']:  # Skip stickied posts
                    print(f"{i}. {child['data']['title']}")
        else:
            print("No hot posts found for this subreddit.")
    else:
        print("None")


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
