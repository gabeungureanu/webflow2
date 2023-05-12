import requests
from bs4 import BeautifulSoup
import os


# url_link = input('Enter the Url:')
url ='https://safelite.webflow.io/'
r = requests.get(url)
    
soup = BeautifulSoup(r.text,"lxml")


links = soup.findAll('img')
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
            #file_path = os.path.join('C:\\Users\\JAI SINGH\\', filename)
            file_path = os.path.join(folder, filename)
            
            # Update the src path
            #link['src'] = file_path
            #response = requests.post(url, data=str(soup))
            # Save the SVG file to the specified folder
            with open(file_path, "wb") as f:
                f.write(response.content)
                
            #img=Image.open(response.raw)
            #for j in range(0,10):
                #img.save('C:\\Users\\JAI SINGH\\image{}.svg'.format(i))
                #cv.SaveImage('pic{:>05}.jpg'.format(i), j) 
        except:
            #print(KeyError)
            val=1
        i += 1


    # get the JavaScript files
script_files = []
for script in soup.find_all("script"):
       if script.attrs.get("src"):
        # if the tag has the attribute 'src'
        script_url = script.attrs.get("src")
        if script_url.find('cloudfront') == -1:    
         script_files.append(script_url)

    
folder = "./js/"
            # Make sure the folder exists
if not os.path.exists(folder):
        os.makedirs(folder)


for js_file in script_files:
     fileName = os.path.basename(js_file)
     file_path = os.path.join(folder, fileName)
     text = requests.get(js_file).text
     with open(file_path, 'w', encoding="utf-8") as f:
        f.write(text)

    # get the CSS files
css_files = []
url ='https://assets.website-files.com/'
r = requests.get(url)
    
soup = BeautifulSoup(r.text,"lxml")
    
for css in soup.find_all("link"):
         if css.attrs.get("href"):
            # if the link tag has the 'href' attribute
            css_url = css.attrs.get("href")
            if css_url.find('css') >= 1:   
             css_files.append(css_url)

folder = "./css/"
            # Make sure the folder exists
if not os.path.exists(folder):
        os.makedirs(folder)

for css_file in css_files:     
     fileName = os.path.basename(css_file)
     file_path = os.path.join(folder, fileName)
     text = requests.get(js_file).text
     with open(file_path, 'w', encoding="utf-8") as f:
        f.write(text)
