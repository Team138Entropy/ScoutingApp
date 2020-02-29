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
subDict={}
#INITIAL EMPTY LIST
rankList = []
global team_arr
global sub_arr
global contT
global contF
contT = 1
contF = 0

url = "https://strategy-e354.restdb.io/rest/strategy"
headers = {
    'content-type': "application/json",
    'x-apikey': "5c807aadcac6621685acbc2f",
    'cache-control': "no-cache"
    }

#variable assignment(leah made)
def convertingVariables():
    global cpVariable
    global mVariable
    global dbVariable
    global fVariable
    global acVariable
    global cVariable
    global mainDict
    global team_arr
    global sub_arr
    #sub 2
    if control_panel == "Neither":
        cpVariable = 0
    elif control_panel == "Rotation":
        cpVariable = 10
    elif control_panel == "Color Pick":
        cpVariable = 20
    elif control_panel == "Both":
        cpVariable = 30
    #sub 3
    if moved == "Moved":
        mVariable = 5
    elif moved == "Didn't move":
        mVariable = 0
    #sub 4
    #points can be replaced
    if defensive_bool == True:
        dbVariable = 10
    elif defensive_bool == False:
        dbVariable = 0
    #sub 5
    if flags == "None":
        fVariable = 0
    elif flags == "Yellow flag":
        fVariable = -10
    elif flags == "Red flag":
        fVariable = -50
    #sub 6
    if climb == "no_climb":
        cVariable = 0
    elif climb == "Climbed":
        cVariable = 25
    elif climb == "Aided Climb":
        cVariable = 10
    #sub 7
    if aided_climb == True:
        acVariable = 40
    elif aided_climb == False:
        acVariable = 0

def teamJazz():
    global team_str
    global contT
    global contF
    global mainDict
    global subDict
    global team_arr
    global sub_arr
    team_str = str(team_tuple)
    if team_str in mainDict:
        sub_arr = ()
        sub_arr = (mainDict[team_str])
        #print(sub_arr)
        convertingVariables()
        sauto = (sub_arr[0]+auto_cells)/2
        stele = (sub_arr[1]+tele_cells)/2
        scont = (sub_arr[2]+cpVariable)/2
        smove = (sub_arr[3]+mVariable)/2
        sdefe = (sub_arr[4]+dbVariable)/2
        sflag = (sub_arr[5]+fVariable)/2
        sclimb = (sub_arr[6]+cVariable)/2
        saide = (sub_arr[7]+acVariable)/2
        mainDict[team_str] = sauto, stele, scont, smove, sdefe, sflag, sclimb, saide
    else:
        convertingVariables()
        mainDict[team_str] = auto_cells, tele_cells, cpVariable, mVariable, dbVariable, fVariable, cVariable, acVariable
    subDict = mainDict

def organize():
    global winning
    global rankList
    sum = 0
    winning = str()
    winArrSum = 0
    sub_arr = ()
    sub_arr = (mainDict[team_str])
    #THIS WORKS - LEAH
    #ASSIGNS EVERYTHING TO AN INITIAL PLACE IN THE LIST
    for i in mainDict:
        if team_str in rankList:
            rankList = rankList
        else:
            rankList.append(team_str)
    #THIS DOES NOT...I THINK... - LEAH
    #THIS SORTS THE DATA WITHIN THE LIST
    #CURRENTLY DEFAULTS TO ELSE CUT THAT MAY ACTUALLY BE RIGHT...YOU MAY NEED TO ADD MORE DATA...
    #TEXT ME IF YOU DONT UNDERSTAND :)
    for j in mainDict:
        sumOne = sub_arr[1]+sub_arr[2]+sub_arr[3]+sub_arr[4]+sub_arr[5]+sub_arr[6]+sub_arr[7]
        for k in mainDict:
            sumTwo = sub_arr[1]+sub_arr[2]+sub_arr[3]+sub_arr[4]+sub_arr[5]+sub_arr[6]+sub_arr[7]
            if sumOne > sumTwo:
                rankList.insert(rankList.index(mainDict[j]), mainDict[i])
            else:
                print(mainDict[k])

@app.route("/data")
def data():
    team_arr = []
    response = requests.request("GET", url, headers=headers)
    for match in json.loads(response.text):
        #globals
        global team_tuple
        global winning
        global rankList
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
        global sub_arr
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
        organize()
    print(winning)
    print (mainDict)
    print(rankList)
    return json.dumps(team_arr)
    return json.dumps(winning)
if __name__ == "__main__":
    app.run()


#TODO after this make it a list for now just print the best
