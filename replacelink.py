import requests
import json



url = 'https://api.github.com/repos/gabeungureanu/webflow2/contents/index.html'
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "Bearer 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"
}

response = requests.get(url, headers=headers)


