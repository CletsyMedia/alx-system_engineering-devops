#!/usr/bin/python3
"""
A function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.
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

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json().get('data', {})
        children = data.get('children', [])
        if children:
            for i, child in enumerate(children[:10], 1):
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
#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit
"""

from requests import get


def top_ten(subreddit):
    """
    function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit
    """

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params)
    results = response.json()

    try:
        my_data = results.get('data').get('children')

        for i in my_data:
            print(i.get('data').get('title'))

    except Exception:
        print("None")
