# find the most starred github repo
def moststars():
    import requests
    import json
    from collections import Counter
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    result = r.json()
    repo_dicts = result['items']
    repo_dict = repo_dicts[0]
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_stars = repo_dict['stargazers_count']
    repo_owner = repo_dict['owner']['login']
    repo_owner_url = repo_dict['owner']['html_url']
    repo_description = repo_dict['description']
    print('The most starred repo is {} with {} stars.'.format(repo_name, repo_stars))
    print('{} can be found at {}'.format(repo_owner, repo_owner_url))
    print('{} can be found at {}'.format(repo_name, repo_url))
    print('{}'.format(repo_description))
    return

# create a list of the 25 most starred github repos
def top25():
    import requests
    import json
    from collections import Counter
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    r = requests.get(url)
    result = r.json()
    repo_dicts = result['items']
    repo_dict = repo_dicts[0]
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_stars = repo_dict['stargazers_count']
    repo_owner = repo_dict['owner']['login']
    repo_owner_url = repo_dict['owner']['html_url']
    repo_description = repo_dict['description']
    repo_list = []
    for repo_dict in repo_dicts:
        repo_list.append(repo_dict['name'])
    print('The 25 most starred repos are:')
    for repo in repo_list:
        print(repo)
    return

# run the function
top25()