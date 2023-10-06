import json 
import sys 
with open('ftp.json') as f: 
   info = json.load(f) 
new_name = info["Filename"] 
d = {} key = 'name' 
d[key] = new_name 
json_object = json.dumps(d, indent = 4) 
print(json_object)
