import requests
import json



url = 'https://api.github.com/repos/gabeungureanu/webflow2/contents/index.html'
headers = {
    "Accept": "application/vnd.github.v3+json",
    "Authorization": "Bearer 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"
}

response = requests.get(url, headers=headers)


