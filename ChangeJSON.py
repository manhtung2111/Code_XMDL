import json 
import sys 
with open('ftp.json', 'r+') as f: 
    info = json.load(f)
new_dir = info["Filename"] 
print(new_dir)
