import os
import json
from github import Github

def get_github_logs(username, repository):
    # Initialize the GitHub API client
    g = Github()
 
    # Get the specified repository
    repo = g.get_repo(f"{username}/{repository}")

    # Get all commits from the repository
    commits = repo.get_commits()
 
    # Convert the commit history to a list of dictionaries
    commit_history = []
    for commit in commits:
        commit_data = {
            "sha": commit.sha,
            "author": commit.author.login if commit.author else "Unknown",
            "message": commit.commit.message,
            "date": commit.commit.author.date.strftime("%Y-%m-%d %H:%M:%S"),            
        }
        commit_history.append(commit_data)

    return commit_history

if __name__ == "__main__":
    username = "gabeungureanu"
    repository = "webflow2"

    history_data = get_github_logs(username, repository)

    # Get the script's directory
    script_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Create a subdirectory named 'data' (if it doesn't exist) to store the JSON file
    data_directory = os.path.join(script_directory, "data")
    os.makedirs(data_directory, exist_ok=True)
    
    # Save the commit history to a JSON file
    json_file_path = os.path.join(data_directory, "github_logs.json")
    with open(json_file_path, 'w') as json_file:
        json.dump(history_data, json_file, indent=4)

    print("Commit history saved to:", json_file_path)
