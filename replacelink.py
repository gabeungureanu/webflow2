import requests
from bs4 import BeautifulSoup
import base64
import json



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
