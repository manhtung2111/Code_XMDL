import sys 
import json 
with open('new_password.json', 'r+') as f: 
    new_info = json.load(f)
new_password = new_info["New_pass"] 
with open('login.json', 'r+') as f: 
    login_info = json.load(f)
login_user = login_info["Username"] 
new_login_info = { "Password": str(new_password), "Username": "test"}
json_object = json.dumps(new_login_info, indent=2)
# Writing to sample.json
with open("login.json", "w") as outfile: 
    outfile.write(json_object)
