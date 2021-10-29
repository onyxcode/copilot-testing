# get a random repo from github and print the url
import requests
import random
import json
import sys
import os
def repo():
    # get a random repo from github
    url = "https://api.github.com/users/{}/repos".format(os.environ.get('GITHUB_USER'))
    response = requests.get(url)
    if response.status_code != 200:
        print("{} {}".format(response.status_code, response.reason))
        sys.exit(1)
    # get the json data
    data = response.json()
    # get a random repo
    repo = random.choice(data)
    # print the url
    print(repo['html_url'])

# run the function
repo()