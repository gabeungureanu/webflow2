import requests
import json



url = 'https://api.github.com/repos/gabeungureanu/webflow2/contents/index.html'
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "Bearer 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"
}

response = requests.get(url, headers=headers)
data = json.loads(response.content)

