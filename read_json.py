import json

file_path = '/home/runner/work/webflow2/webflow2/recipients.json'  # Replace with the actual path to your JSON file

try:
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
        recipients = data['json_data']
         concatenated = ', '.join(recipient['email'] for recipient in recipients)
        Emaildata = concatenated
         #print(f"::set-output name=data::{json_data}")
        #print(json_data)
except Exception as e:
    print(f"Error reading JSON file: {e}")
    exit(1)
