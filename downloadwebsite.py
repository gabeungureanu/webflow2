import os
import requests
from urllib.parse import urlparse, urljoin

def download_page(url, base_url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Create the corresponding directory structure
    file_path = os.path.join(parsed_url.netloc, parsed_url.path.strip('/'))
    if not parsed_url.path or parsed_url.path.endswith('/'):
        # If the URL represents the root page or a directory, append index.html
        file_path = os.path.join(file_path, 'index.html')
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Make the HTTP request
    response = requests.get(url)

    # Save the response content to a file
    with open(file_path, 'wb') as file:
        file.write(response.content)

def download_website(url):
    # Make the initial request to get the base URL
    response = requests.get(url)

    # Extract the base URL from the response
    base_url = response.url

    # Download the base URL
    download_page(base_url, base_url)

    # Parse the HTML content of the base URL
    html_content = response.text

    # Extract all links from the HTML content
    links = extract_links(html_content)

    # Download all linked pages recursively
    for link in links:
        absolute_url = urljoin(base_url, link)
        download_page(absolute_url, base_url)

def extract_links(html_content):
    # Add your logic to extract links from the HTML content
    # This can be done using libraries like BeautifulSoup or regular expressions
    # For demonstration purposes, we assume a dummy list of links
    links = [
        '/index.html',
        '/help-center',
        '/vehicles'
         '/robots.txt',
    '/vehicle-make/acura.html',
    '/vehicle-make/audi.html',
    '/vehicle-make/bmw.html',
    '/vehicle-make/buick.html',
    ]
    return links

# Example usage
url = 'https://safelite.webflow.io'

# Download the website
download_website(url)
