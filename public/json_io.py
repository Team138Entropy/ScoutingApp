import json
from flask import Flask
import requests


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
    team_arr = []
    response = requests.request("GET", url, headers=headers)
    for match in json.loads(response.text):
        team_num = "team_number"
        team_tuple = match[team_num]
        team_arr.append(team_tuple)
    return json.dumps(team_arr)
if __name__ == "__main__":
    app.run()
