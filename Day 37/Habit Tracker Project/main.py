#using the PIXELA API https://pixe.la/
import requests
import os
from datetime import datetime


PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
USER_NAME = os.environ.get("PIXELA_USER_NAME")
GRAPH_ID = "graph1"


#----------------- CREATE USER --------------------------------------#
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

#---------------------- CREATE GRAPH -----------------------------------#
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config= {
    "id": "graph1",
    "name": "Reading Neuromancer",
    "unit": "Page",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

#------------------------- ADD PIXEL TO GRAPH ------------------------------------#
add_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

#for today, use today.strftime
#for other day, change to other_day.strftime and add the date into the datetime tuple.

today = datetime.now()
#other_day =datetime(year=, month=, day=)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1",
}

response = requests.post(url=add_pixel_endpoint, json=pixel_data, headers=headers)
print(response.text)

#---------------------- CHANGE AND DELETE PIXEL FROM GRAPH ------------------------#

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "2",
}

#response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
#print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)