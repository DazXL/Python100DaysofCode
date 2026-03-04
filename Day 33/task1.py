#Task 1 is about API requests

import requests #https://pypi.org/project/requests/

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status() #raises exception if an error happens

data = response.json()

print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

print(f"ISS current position is:{iss_position}")
