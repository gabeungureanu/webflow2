import json

file_path = '/home/runner/work/webflow2/webflow2/recipients.json'  # Replace with the actual path to your JSON file

try:
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

# Iterate through the array and concatenate values
concatenated = ""
for item in json_data:
    concatenated += item['email'] + ", "

# Remove the trailing comma and space
concatenated = concatenated.rstrip(', ')
        print(json.dumps(concatenated))  # Return the JSON data as a string
except Exception as e:
    print(f"Error reading JSON file: {e}")
    exit(1)
