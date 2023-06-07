import os
import subprocess
from bs4 import BeautifulSoup

# Define the git command to list all HTML files
git_cmd = 'git ls-files "*.html"'

# Execute the git command and get the output
output = subprocess.check_output(git_cmd, shell=True).decode().strip()

# Split the output into a list of HTML file paths
html_files = output.split('\n')

# Loop through each HTML file
for html_file in html_files:
    # Read the HTML file
    with open(html_file, 'r') as file:
        html = file.read()

    # Parse the HTML
    soup = BeautifulSoup(html, 'html.parser')

    # Find all img tags
    img_tags = soup.find_all('img')

    # Loop through the img tags and remove the srcset attribute
    for img in img_tags:
        if 'srcset' in img.attrs:
            del img.attrs['srcset']

    # Get the modified HTML
    modified_html = str(soup)

    # Write the modified HTML back to the file
    with open(html_file, 'w') as file:
        file.write(modified_html)
