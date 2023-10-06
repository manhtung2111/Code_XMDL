import sys
import json 
Password_data = json.loads(sys.argv[1]) 
Pass_input = Password_data["New_pass"] 
Pass_input_confirm = Password_data["New_pass_confirm"] 
Oldpass_input = Password_data["Old_pass"] 
with open('login.json', 'r+') as f:
    info = json.load(f) 
old_password = info["Password"] 
if Pass_input == Pass_input_confirm and old_password == Oldpass_input :
    new_login_info = { "Password": str(Pass_input), "Username": "test"}
    json_object = json.dumps(new_login_info, indent=2)
# Writing to sample.json
    with open("login.json", "w") as outfile: 
      outfile.write(json_object) 
    print(1)
else:
    print(2)
