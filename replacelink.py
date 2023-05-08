import requests
import base64

# Set up authentication credentials
user = 'gabeungureanu'
token = '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'
headers = {'Authorization': f'token {token}'}


# Define the repository and file to retrieve
repo_owner = 'gabeungureanu'
repo_name = 'webflow2'
file_path = 'index.html'


# Define the new content for the file
new_content = 'This is the new content of the file'

# Make an API request to get the current content of the file
url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
response = requests.get(url, headers=headers)

# Get the SHA of the file for the update request
sha = response.json()['sha']

# Decode the content of the file
content = base64.b64decode(response.json()['content']).decode('utf-8')

# Replace the content with the new content
updated_content = content.replace(content, new_content)

# Encode the updated content in Base64 format
encoded_content = base64.b64encode(updated_content.encode('utf-8')).decode('utf-8')

# Define the API endpoint and payload for updating the file
api_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path}'
payload = {
    'message': 'Update file content',
    'content': encoded_content,
    'sha': sha
}

# Make an API request to update the file content
response = requests.put(api_url, headers=headers, json=payload)
