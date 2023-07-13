import json

file_path = ${{ github.workspace }}'/blob/main/recipients.json'  # Replace with the actual path to your JSON file

try:
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)
        print(json_data)
except Exception as e:
    print(f"Error reading JSON file: {e}")
    exit(1)
