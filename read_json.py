import json

file_path = '/home/runner/work/webflow2/webflow2/recipients.json'  # Replace with the actual path to your JSON file

try:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        recipients = data['recipients']
        concatenated = ', '.join(recipient['email'] for recipient in recipients)
        print(concatenated)
        output_data = json.dumps(concatenated)
        # Set the output
        print(f"::set-output name=output_data::{output_data}")
except Exception as e:
    print(f"Error reading JSON file: {e}")
    exit(1)
