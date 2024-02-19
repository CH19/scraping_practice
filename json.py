import json
new_json = json()
json_files = open("youtubers.json", "r")
json_read = json_files.read()
data = new_json.loads(json_read)
print(data)