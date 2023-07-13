import json

file_path = '/home/runner/work/webflow2/webflow2/recipients.json'  # Replace with the actual path to your JSON file

try:
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
        for item in data:
            print(item)
except Exception as e:
    print(f"Error reading JSON file: {e}")
    exit(1)
