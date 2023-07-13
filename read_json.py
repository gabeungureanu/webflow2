import json

file_path = '/home/runner/work/webflow2/webflow2/recipients.json'  # Replace with the actual path to your JSON file

try:
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
        # Parse the JSON data
        parsed_data = json.loads(data)
        # Extract the email list
        email_list = [recipient['email'] for recipient in parsed_data['recipients']]
print(email_list)

except Exception as e:
    print(f"Error reading JSON file: {e}")
    exit(1)
