import json
file_path = '/home/runner/work/webflow2/webflow2/recipients.json'
def read_json_file(file_path):
    with open(file_path) as file:
       data = json.load(json_file)
        recipients = data['recipients']
        concatenated = ', '.join(recipient['email'] for recipient in recipients)
       print(concatenated)        
except Exception as e:
    print(f"Error reading JSON file: {e}")
    exit(1)
