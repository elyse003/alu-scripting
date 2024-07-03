#!/usr/bin/python3
'''
    This module contains the function number_of_subscribers
'''

import requests
from sys import argv

def number_of_subscribers(subreddit):
    '''
        Returns the number of subscribers for a given subreddit
    '''
    user_agent = {'User-Agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=user_agent, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.exceptions.RequestException:
        return 0

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script_name.py subreddit_name")
        exit(1)
    subreddit_name = argv[1]
    subscriber_count = number_of_subscribers(subreddit_name)
    print(subscriber_count)

