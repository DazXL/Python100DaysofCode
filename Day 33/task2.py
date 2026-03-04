#Task 2 is about API request with arguments
import requests
from datetime import datetime

MY_LAT = -22.906847
MY_LONG = -43.172897



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]



print(f"Sunrise: {sunrise} | Sunset: {sunset}")

time_now = datetime.now()
print(f"Time now: {time_now.hour}")