import json
from flask import Flask
import requests
#import json

team_arr = []

app = Flask(__name__)
app.config['TESTING'] = True

url = "https://strategy-e354.restdb.io/rest/strategy"
headers = {
    'content-type': "application/json",
    'x-apikey': "5c807aadcac6621685acbc2f",
    'cache-control': "no-cache"
    }

@app.route("/data")
def data():
    response = requests.request("GET", url, headers=headers)
    for match in json.loads(response.text):
        # team_num = int("team_number")
        team_num = "team_number"
        team_tuple = match[team_num]
        print("get me out of here")
        team_arr.append(team_tuple)
    return json.dumps(team_arr)
if __name__ == "__main__":
    app.run()
