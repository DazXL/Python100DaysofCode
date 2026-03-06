#Task 3 is unifying the task 1 and two, so an SMS can be sent when it is raining to remind us to get an umbrella
#Also making use of environment variables so no sensitive data is leaked
import os #used to access the environment variables
from twilio.rest import Client
import requests

lat = os.environ.get("LAT")
lon = os.environ.get("LON")
api_key = os.environ.get("OWM_API_KEY")#register at https://openweathermap.org/ and get your own API key

#twilio params
#register at https://www.twilio.com/
account_sid = os.environ.get("TWI_ACC_SID")#your SID
auth_token = os.environ.get("TWI_AUTH_TOKEN") #your Auth token

#requests params
parameters = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude":"current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
#print(data) #copy and paste for view on https://jsonviewer.stack.hu/
#print(data["list"][0]["weather"][0]["id"])

will_rain = False

for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    #print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It might rain! Bring an Umbrella!! ☔.",
        from_=os.environ.get("TWILIO_NUMBER"), #add your twilio number
        to=os.environ.get("MY_NUMBER"), #add your own number
    )

    print(message.status)