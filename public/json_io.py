from flask import Flask
import requests

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
    return response.text
if __name__ == "__main__":
    app.run()
