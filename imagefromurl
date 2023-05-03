import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
import shutil # to save it locally
from urllib.request import urlopen, Request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://gabriels-fantabulous-site-23ac8b.webflow.io/"
req = Request(url=url, headers=headers)
html = urlopen(req).read()
soup = BeautifulSoup(html,'html.parser')
tags = soup('img')
i = 1
for tag in tags:
    # Set up the image URL and filenameht
    image_url = tag.get('src',None)
    # print(image_url)
    filename = "image" + str(i) + ".jpeg"
    # Open the url image, set stream to True, this will return the stream content.
    try:
        r = requests.get(image_url, stream = True)
    except:
        pos = image_url.find("http")
        image_url = image_url[pos:]
        r = requests.get(image_url, stream = True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)        
    else:
        print('Image Couldn\'t be retreived')
    i += 1
