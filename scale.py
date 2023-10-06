import sys 
import json 

scale_data = json.loads(sys.argv[1])
scale_temp = scale_data["scale_temp"]
offset_temp = scale_data["offset_temp"]
scale_press = scale_data["scale_press"]
offset_press = scale_data["offset_press"]
scale_flow = scale_data["scale_flow"]
offset_flow = scale_data["offset_flow"]
scale_pm = scale_data["scale_pm"]
offset_pm = scale_data["offset_pm"]

scale_data = {
    "scale_temp":scale_temp,
    "offset_temp":offset_temp,
    "scale_press":scale_press,
    "offset_press":offset_press,
    "scale_flow":scale_flow,
    "offset_flow":offset_flow,
    "scale_pm":scale_pm,
    "offset_pm":offset_pm,
    }
json_data = json.dumps(scale_data,indent=8)
with open("scale.json","w") as f:
    f.write(json_data)
