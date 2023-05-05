import requests
from bs4 import BeautifulSoup
import os
import base64
import json
import re


url = 'https://api.github.com/repos/gabeungureanu/webflow2/contents/index.html'
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "Bearer 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"
}

response = requests.get(url, headers=headers)
data = json.loads(response.content)

content = base64.b64decode(data['content']).decode('utf-8')
#content = content.replace("old_content", "new_content")
content = content.replace("https://uploads-ssl.webflow.com/63ff41bea75a04f76f8bbd7a", "images")
content = content.replace("https://uploads-ssl.webflow.com/63ff41bea75a049e418bbd55", "images")
#content = content.replace("https://uploads-ssl.webflow.com/63ff41bea75a049e418bbd55", "images/")


new_content = base64.b64encode(content.encode('utf-8')).decode('utf-8')
data = {
    "message": "Update file",
    "content": new_content,
    "sha": data['sha']
}

response = requests.put(url, headers=headers, json=data)



if response.status_code == 200:
    print('File updated successfully!')
else:
    print('An error occurred while updating the file:', response.content)
