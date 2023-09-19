import os
import requests
from bs4 import BeautifulSoup
import git

def track_website_changes(website_url):
    # Specify the path to your existing Git repository
    repo_path = '.git'

    # Fetch the website content
    response = requests.get(website_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract and process web content here

        # Initialize the Git repository
        repo = git.Repo(repo_path)

        # Stage all changes
        repo.index.add('*')

        # Commit changes
        repo.index.commit("Update website content")

        # Push to remote repository (if applicable)
        origin = repo.remote(name='origin')
        origin.push()
        
        # Delete downloaded files to keep the workspace clean
        for file in os.listdir(repo_path):
            file_path = os.path.join(repo_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    else:
        print(f"Failed to fetch {website_url}")

# Example usage:
website_url = 'http://mattrichmond.ca'
track_website_changes(website_url)
