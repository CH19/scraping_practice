import json
json_files = open("youtubers.json", mode="r")
jso_read = json_files.read()
data = json.loads(jso_read)
print(data)