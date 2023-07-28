import json
import os

#def get_pushed_files():
#    try:
#        event_path = os.environ["GITHUB_EVENT_PATH"]
#        with open(event_path, 'r') as event_file:
#            event_data = json.load(event_file)
#        return event_data["commits"][0]["added"] + event_data["commits"][0]["modified"] + event_data["commits"][0]["removed"]
#    except Exception as e:
#        print(f"Failed to get pushed files: {e}")
#        return []

def add_data_to_audit_log(new_data):
    file_path = "python/audit_log.json"

    # Step 1: Read the existing JSON data from the file (if it exists)
    try:
        if os.path.exists(file_path):
            with open(file_path, 'r') as json_file:
                existing_data = json.load(json_file)
        else:
            existing_data = []
    except FileNotFoundError:
        existing_data = []

    # Step 2: Append the new data to the existing data
    existing_data.append(new_data)

    # Step 3: Write the updated data back to the JSON file
    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

if __name__ == "__main__":
    # Get the list of files pushed in the event
    #pushed_files = get_pushed_files()

    # Sample new data to add to the audit log
    new_data = {
        "event": "new_event",
        "timestamp": "2023-07-27T12:34:56Z",
        "details": "Some details about the new event",
        #"files": pushed_files
    }

    add_data_to_audit_log(new_data)
