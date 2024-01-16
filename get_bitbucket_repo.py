import requests
import os
import subprocess
import sys
import time

url_file = "clone_urls"
destination_folder = sys.argv[1] if len(sys.argv) > 2 else "bitbucket_repo"
next_page = 'https://api.bitbucket.org/2.0/repositories'

if os.path.exists(url_file):
    with open(url_file, 'r', encoding="utf-8")as r:
        repo_urls = [i.strip() for i in r.readlines()]
    print("repos list already exists, clone repos now")

else:
    repo_urls = list()
    err_count = 0
    counter = 0
    while next_page:
        try:
            time.sleep(2)
            response = requests.get(next_page)  #, auth=(username, password))
            repos = response.json()['values']
            repo_urls += [repo['links']['clone'][0]['href'] for repo in repos]
            next_page = response.json().get("next")
            counter += 1
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S')} crawl a new page, page count {counter}")
            err_count = 0
        except:
            err_count += 1
            if err_count >= 3: break
    with open(url_file, 'w', encoding="utf-8")as w:
        w.write("\n".join(repo_urls))


# Clone each repository into the specified folder
for url in repo_urls:
    time.sleep(1)
    repo_name = url.split('/')[-1].replace('.git', '') # Extract repository name from URL
    org_name = url.split('/')[-2]
    clone_path = os.path.join(destination_folder, org_name, repo_name)
    os.makedirs(os.path.dirname(clone_path), exist_ok=True)
    subprocess.run(['git', 'clone', url, clone_path])
