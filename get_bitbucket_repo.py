import requests
import os
import subprocess
import sys

url = 'https://api.bitbucket.org/2.0/repositories'

destination_folder = sys.argv[1] if len(sys.argv) > 2 else "bitbucket_repo"
response = requests.get(url) #, auth=(username, password))

repos = response.json()['values']
repo_urls  = [repo['links']["clone"][0]["href"] for repo in repos]

# Handle pagination if necessary
next_page = response.json().get('next')
while next_page:
    response = requests.get(next_page) #, auth=(username, password))
    repos = response.json()['values']
    repo_urls += [repo['links']["clone"][0]["href"] for repo in repos]
    next_page = response.json().get('next')

# Clone each repository into the specified folder
for url in repo_urls:
    repo_name = url.split('/')[-1].replace('.git', '') # Extract repository name from URL
    org_name = url.split('/')[-2]
    clone_path = os.path.join(destination_folder, org_name, repo_name)
    os.makedirs(os.path.dirname(clone_path), exist_ok=True)
    subprocess.run(['git', 'clone', url, clone_path])
