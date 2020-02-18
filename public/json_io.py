import json
from flask import Flask
import requests

app = Flask(__name__)
app.config['TESTING'] = True

#vars
team_num = "team_number"
move_num = "move_off_line"
autoL_num = "auto_LowerPort"
autoU_num = "auto_UpperPort"
autoI_num = "auto_InnerPort"
teleL_num = "teleop_LowerPort"
teleU_num = "teleop_UpperPort"
teleI_num = "teleop_InnerPort"
control_num = "Control_Panel"
defensive_num = "was_defensive"
aided_num = "Aided_climb"
flags_num = "flags"
climb_num = "final_climb_level"
mainDict ={}
global contT
global contF
contT = 0
contF = 0

url = "https://strategy-e354.restdb.io/rest/strategy"
headers = {
    'content-type': "application/json",
    'x-apikey': "5c807aadcac6621685acbc2f",
    'cache-control': "no-cache"
    }
def teamJazz():
    global team_str
    team_str = str(team_tuple)
    if team_str in mainDict:
        sub_arr = ()
        sub_arr = (mainDict[team_str])
        print(sub_arr)
        for i in sub_arr:
            sauto = (sub_arr[0]+auto_cells)/2
            stele = (sub_arr[1]+tele_cells)/2
            if (contT>contF):
                scont = True
                contT += 1 
            elif (contF>contT):
                scont = False
                contF += 1
            scont = (sub_arr[2]+control_panel)/2
            smove = (sub_arr[3]+moved)/2
            sdefe = (sub_arr[4]+defensive_bool)/2
            sflag = (sub_arr[5]+flags)/2
            sclimb = (sub_arr[5]+climb)/2
            saide = (sub_arr[6]+aided_climb)/2
            mainDict[team_str] = sauto, stele, scont, smove, sdefe, sflag, sclimb, saide
    else:
        mainDict[team_str] = auto_cells, tele_cells, control_panel, moved, defensive_bool, flags, climb, aided_climb
@app.route("/data")
def data():
    team_arr = []
    response = requests.request("GET", url, headers=headers)
    for match in json.loads(response.text):
        #globals
        global team_tuple
        #cell stuff
        global auto_lower
        global auto_upper 
        global auto_inner 
        global tele_lower 
        global tele_upper 
        global tele_inner 
        global auto_cells 
        global tele_cells
        global cell_points
        #not cell stuff
        global control_panel
        global defensive_bool
        global flags
        global climb
        global aided_climb
        global moved
        moved = match[move_num]
        aided_climb = match[aided_num]
        climb = match[climb_num]
        flags = match[flags_num]
        control_panel = match[control_num]
        defensive_bool = match[defensive_num]
        team_tuple = match[team_num]
        auto_lower = match[autoL_num]
        auto_upper = match[autoU_num] 
        auto_inner = match[autoI_num]
        tele_lower = match[teleL_num]
        tele_upper = match[teleU_num]
        tele_inner = match[teleI_num]
        auto_cells = auto_lower+auto_upper+auto_inner
        tele_cells = tele_lower+tele_upper+tele_inner
        cell_points = (auto_cells * 2)+tele_cells
        team_arr.append(team_tuple)
        teamJazz()
    print (mainDict)
    return json.dumps(team_arr)
if __name__ == "__main__":
    app.run()








global auto_lower
global auto_upper 
global auto_inner 
global tele_lower 
global tele_upper 
global tele_inner 
global auto_cells 
global tele_cells