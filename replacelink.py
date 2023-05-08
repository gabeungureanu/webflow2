

# Set up authentication credentials
user = 'gabeungureanu'
token = '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'
headers = {'Authorization': f'token {token}'}


# Define the repository and file to retrieve
repo_owner = 'gabeungureanu'
repo_name = 'webflow2'
file_path = 'index.html'


# Make the API request to retrieve the file contents
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
response = requests.get(url, headers=headers)

# Extract the file content from the API response
file_content = response.json()['content']

# Decode the base64-encoded file content
content = base64.b64decode(file_content).decode('utf-8')
