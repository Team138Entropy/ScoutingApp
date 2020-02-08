import requests


url = "https://strategy-e354.restdb.io/rest/strategy"

headers = {
    'content-type': "application/json",
    'x-apikey': "5c807aadcac6621685acbc2f",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
