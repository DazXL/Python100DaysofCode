#This project makes use of a few APIs, the 100days API uses natural language to give results using AI

import requests
from datetime import datetime
import os

#from https://app.100daysofpython.dev/
API_ID=os.environ.get("HDAYS_API_ID")
API_KEY=os.environ.get("HDAYS_API_KEY")

##### APP CONSTANTS
GENDER = os.environ.get("GENDER")
WEIGHT_KG = int(os.environ.get("WEIGHT_KG"))
HEIGHT_CM = int(os.environ.get("HEIGHT_CM"))
AGE = int(os.environ.get("AGE"))

##### Time variables
date = datetime.now().strftime("%d/%m/%Y")
time = datetime.now().strftime("%H:%M:%S")

#### Requests to the 100days API
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")

workout_headers = {
    "Content-Type": "application/json",
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

workout_parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

#### testing 100 days API response
# workout_response = requests.get(os.environ.get("https://app.100daysofpython.dev/healthz"))
# print(workout_response.text)

##### POST to generate exercise results
response = requests.post(exercise_endpoint, json=workout_parameters, headers=workout_headers)
result = response.json()

# print(result)

##### SHEETY API to add results to the Google spreadsheet
# sheety API: https://sheety.co/
# copy it from here https://docs.google.com/spreadsheets/d/1DHL6Y8XAHSC_KhJsa9QMekwP8b4YheWZY_sxlH3i494/

sheety_endpoint = os.environ.get("SHEETY_ENDPOINT")

headers = {
    'Authorization': f'Bearer {os.environ.get("SHEETY_BEARER_TOKEN")}',
}

sheety_body = {
    'workout': {
        'date': date,
        'time': time,
        'exercise': result['exercises'][0]['name'].title(),
        'duration': result['exercises'][0]['duration_min'],
        'calories': result['exercises'][0]['nf_calories'],
    }
}

##### Test the API with GET
# sheety_test = requests.get(sheety_endpoint)
# print(sheety_test.json())

##### POST so the API add results to the google sheet
sheety_response = requests.post(sheety_endpoint, headers=headers, json=sheety_body)
print(sheety_response.text)