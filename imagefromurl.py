import requests
from bs4 import BeautifulSoup
from PIL import Image
import os

# url_link = input('Enter the Url:')
r = requests.get('https://gabriels-fantabulous-site-23ac8b.webflow.io/')

soup_obj = BeautifulSoup(r.text,"lxml")
links = soup_obj.findAll('img')

i = 1

for link in links:
    try:
        src=link['src']
        print(src)
        folder = "./images/"
        # Make sure the folder exists
        if not os.path.exists(folder):
            os.makedirs(folder)

        response = requests.get(src,stream=True)        
        # Construct the full path to save the file
        filename = os.path.basename(src)
        file_path = os.path.join(folder, filename)
        
        # Save the SVG file to the specified folder
        with open(file_path, "wb") as f:
            f.write(response.content)
            
        #img=Image.open(response.raw)
        #for j in range(0,10):
            #img.save('C:\\Users\\JAI SINGH\\image{}.svg'.format(i))
            #cv.SaveImage('pic{:>05}.jpg'.format(i), j) 
    except:
        print(KeyError)
    i += 1

