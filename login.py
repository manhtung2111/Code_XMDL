import sys 
import json 
login_data = json.loads(sys.argv[1]) 
User_input = login_data["Username"] 
Pass_input = login_data["Password"] 
with open('login.json') as f:
    data = json.loads(f.read())
# FTP server credentials
User_name = data["Username"] 
Pass_word = data["Password"] 
if User_input == User_name and Pass_input == Pass_word:
    print(1) 
elif User_input != User_name or Pass_input != Pass_word: 
    print(2)
