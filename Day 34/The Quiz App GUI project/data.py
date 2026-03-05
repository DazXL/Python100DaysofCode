#comparing with the project from Day 17
#instead of fixed questions from a dictionary we use the API to request new questions every time the app runs
import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()

question_data = data["results"]


