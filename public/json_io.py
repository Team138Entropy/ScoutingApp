from flask import Flask
import requests
#import json

team_arr = []

app = Flask(__name__)

url = "https://strategy-e354.restdb.io/rest/strategy"
headers = {
    'content-type': "application/json",
    'x-apikey': "5c807aadcac6621685acbc2f",
    'cache-control': "no-cache"
    }

@app.route("/data")
def data():
    response = requests.request("GET", url, headers=headers)
    for row in response.text:
        team_tuple = (row["team_number"])
        team_arr.append(team_tuple)
    return team_arr
if __name__ == "__main__":
    app.run()
