import json

def add_data_to_audit_log(new_data):
    file_path = "audit_log.json"

    # Step 1: Read the existing JSON data from the file (if it exists)
    try:
        with open(file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = []

    # Step 2: Append the new data to the existing data
    existing_data.append(new_data)

    # Step 3: Write the updated data back to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

if __name__ == "__main__":
    # Sample new data to add to the audit log
    new_data = {
        "event": "new_event",
        "timestamp": "2023-07-27T12:34:56Z",
        "details": "Some details about the new event"
    }

    add_data_to_audit_log(new_data)
