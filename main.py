# Libraries
import requests
from datetime import datetime
# Constants
from secrets import *


# create user
pixela_endpoint = "https://pixe.la/v1/users"
headers = {
    "X-USER-TOKEN": TOKEN,
}
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# create graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "CS Graph",
    "unit": "time",
    "type": "int",
    "color": "ajisai"
}
response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
print(response.text)


# add entry
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "65",
}
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)


# make an edit
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "90"
}
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)


# delete an entry
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
