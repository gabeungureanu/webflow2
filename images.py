import requests
from bs4 import BeautifulSoup
import os

# List of URLs of pages with images
urls = ["https://safelite.webflow.io/", "https://safelite.webflow.io/help-center","https://safelite.webflow.io/vehicles"]

# Path to the folder where images will be saved
folder_path = "./images"

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

Jsfolder = "./js/"
# Make sure the folder exists
if not os.path.exists(Jsfolder):
        os.makedirs(Jsfolder)

cssfolder = "./css/"
# Make sure the folder exists
if not os.path.exists(cssfolder):
        os.makedirs(cssfolder)
# Loop through the URLs
for url in urls:
    # Make a GET request to the URL
    response = requests.get(url)

    # Use BeautifulSoup to parse the HTML response
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all image tags
    image_tags = soup.find_all("img")

    # Loop through the image tags
    for image_tag in image_tags:
        #remove srcset tag
       # Download from srcset attribute
        srcset = image_tag.get('srcset')
        if srcset:
            srcset_urls = [url.strip().split(' ')[0] for url in srcset.split(',')]
            for i, srcset_url in enumerate(srcset_urls):
                image_name = srcset_url.split('/')[-1]
                save_path = os.path.join(folder_path, f"{image_name}")               
                image_response = requests.get(url, stream=True)
                 # Save the image in the folder
                image_response.raise_for_status()
                with open(save_path, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
        
        # Get the source URL of the image
        image_url = image_tag.get("src")

        # Make a GET request to the image URL
        image_response = requests.get(image_url)

        # Extract the filename from the URL
        filename = os.path.basename(image_url)

        # Save the image in the folder
        with open(os.path.join(folder_path, filename), "wb") as f:
            f.write(image_response.content)


    # get the JavaScript files
    script_files = []
    for script in soup.find_all("script"):
       if script.attrs.get("src"):
        # if the tag has the attribute 'src'
        script_url = script.attrs.get("src")
        if script_url.find('cloudfront') == -1:    
         script_files.append(script_url)


    for js_file in script_files:
     fileName = os.path.basename(js_file)
     file_path = os.path.join(Jsfolder, fileName)
     text = requests.get(js_file).text
     with open(file_path, 'w', encoding="utf-8") as f:
        f.write(text)

    #CSS REGION
    # get the CSS files
    css_files = []
    for css in soup.find_all("link"):
         if css.attrs.get("href"):
             # if the link tag has the 'href' attribute
             css_url = css.attrs.get("href")
             if css_url.find('css') >= 1:   
              css_files.append(css_url)

    for css_file in css_files:     
     fileName = os.path.basename(css_file)
     file_path = os.path.join(cssfolder, fileName)
     text = requests.get(js_file).text
     with open(file_path, 'w', encoding="utf-8") as f:
        f.write(text)
