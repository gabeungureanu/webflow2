import json

# Sample JSON array with single property items
json_data = '''
[
    {"email": "john@example.com"},
    {"email": "jane@example.com"},
    {"email": "bob@example.com"}
]
'''

# Parse the JSON array
data = json.loads(json_data)

# Concatenate single property values
concatenated = ', '.join(recipient['email'] for recipient in data)

print(concatenated)
