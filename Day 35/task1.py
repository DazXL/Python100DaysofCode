#Task 1 is using API keys

import requests

lat = -22.906847 #YOU can add your own localization here
lon = -43.172897 #You can add your own localization here

api_key = "YOUR_OWN_API_KEY" #register at https://openweathermap.org/ and get your own API key

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
print(data) #copy and paste for view on https://jsonviewer.stack.hu/
print(data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella")