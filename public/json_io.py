import json
from flask import Flask
import requests

app = Flask(__name__)
app.config['TESTING'] = True

#vars
team_num = "team_number"
autoL_num = "auto_LowerPort"
autoU_num = "auto_UpperPort"
autoI_num = "auto_InnerPort"
move_num = "move_off_line"
teleL_num = "teleop_LowerPort"
teleU_num = "teleop_UpperPort"
teleI_num = "teleop_InnerPort"
control_num = "Control_Panel"
defensive_num = "was_defensive"
aided_num = "Aided_climb"
flags_num = "flags"
climb_num = "final_climb_level"
#ints
auto_lower= int()
auto_upper= int()
auto_inner= int()
tele_lower= int()
tele_lower= int()
tele_upper= int()
tele_inner= int()
auto_cells= int()
tele_cells = int()
#not ints
control_panel = str()
defensive_num = False
flags = str()
moved = str()
aided_climb = False
climb = str()

majorDict ={}

url = "https://strategy-e354.restdb.io/rest/strategy"
headers = {
    'content-type': "application/json",
    'x-apikey': "5c807aadcac6621685acbc2f",
    'cache-control': "no-cache"
    }
def teamJazz():
    team_str = str(team_tuple)
    if team_str in majorDict:
        print("if")
    else:
        print("else")
@app.route("/data")
def data():
    team_arr = []
    response = requests.request("GET", url, headers=headers)
    for match in json.loads(response.text):
        global team_tuple        
        team_tuple = match[team_num]
        auto_lower = match[autoL_num]
        auto_upper = match[autoU_num] 
        auto_inner = match[autoI_num]
        tele_lower = match[teleL_num]
        tele_upper = match[teleU_num]
        tele_inner = match[teleI_num]
        auto_cells = (auto_lower+auto_upper+auto_inner)
        tele_cells = (tele_lower+tele_upper+tele_inner)
        team_arr.append(team_tuple)
        teamJazz()
    return json.dumps(team_arr)
if __name__ == "__main__":
    app.run()
