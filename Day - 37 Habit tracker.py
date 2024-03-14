import requests
from datetime import datetime

USERNAME = "Your username"
TOKEN = "Your token"
GRAPH_ID = "Your Graph ID"

# Define Pixela endpoint
pixela_endpoint = "https://pixe.la/v1/users"

# User creation parameters
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# Uncomment to create user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Define graph endpoint
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

# Graph configuration
graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# Uncomment to create graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Pixel creation endpoint
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

# Pixel data input
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

# Send pixel creation request
response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# Pixel update endpoint
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data = {
    "quantity": "4.5"
}

# Uncomment to update pixel
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Pixel delete endpoint
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# Uncomment to delete pixel
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
