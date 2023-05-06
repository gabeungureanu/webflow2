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

