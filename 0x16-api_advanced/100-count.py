#!/usr/bin/python3
"""
This script defines a function to print a sorted count of given keywords
present inside a given subreddit using recursion
"""


def count_words(subreddit, word_list, after='start', words_count=None):
    """
    Prints sorted count of given words present in subreddit's hot titles
    using the reddit API

    Example:
    >>> words_list = ["react", "python", "java"]
    >>> count("programming", words_list)
    java: 27
    python: 17
    react: 17

    Args:
    subreddit (str): The subreddit to be searched for
    word_list (list): List of keywords to count
    after (str): Index to keep tack of remaining pages `NOT TO BE CHANGED`
    words_count (dict): Keep track of word's count `NOT TO BE CHANGED`

    Returns
    int: 1 valid subreddit or 0 for invalid subreddit

    NOTE:
    The function prints the count result internally
    """
    import requests

    if not word_list:
        return 0

    if words_count is None:
        words_count = {word: 0 for word in word_list}

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"user-agent": "Fake-Agent"}
    if after != 'start':
        url += "?after={}".format(after)

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    for post in response.json().get('data').get('children'):
        title = post.get('data').get('title')
        for word in title.split():
            if word in words_count.keys():
                words_count[word] += 1

    after = response.json().get('data').get('after')
    if after:
        return count_words(subreddit, word_list, after, words_count)
    else:
        words_count = dict(sorted(words_count.items(),
                                  key=lambda x: x[1], reverse=True))
        copy = dict()
        for word, count in words_count.items():
            if word.lower() in copy.keys():
                copy[word.lower()] += count
            else:
                copy[word.lower()] = words_count[word]

        for word, count in copy.items():
            if count != 0:
                print(str(word) + ": " + str(count))
        return 1
