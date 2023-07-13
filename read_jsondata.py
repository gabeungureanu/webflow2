import json

def read_json_file(file_path):
    with open(file_path) as file:
       data = json.load(json_file)
        recipients = data['recipients']
        concatenated = ', '.join(recipient['email'] for recipient in recipients)
        return concatenated
