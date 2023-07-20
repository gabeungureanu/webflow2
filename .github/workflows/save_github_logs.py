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
    print (history_data)
    # Save the commit history to a JSON file
    with open("/home/runner/work/webflow2/webflow2/github_logs.json", 'w') as file:
        json.dump(history_data, file, indent=4)
