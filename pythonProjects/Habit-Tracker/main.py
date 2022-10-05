import requests
from datetime import datetime

TOKEN = "_________ TOKEN ____________"
USERNAME = "_________ USERNAME _________"
GRAPH_ID = "__________ GRAPHID __________"
# GRAPH_ID = "__________ GRAPHID __________"

# ------------------- creating account -------------- #
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# ---------------- creation of graph using post method ----------------- #
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    # "name": "Exercise Graph",
    # "unit": "calory",
    # "type": "int",
    "name": "Cycling Graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


# ---------------------- pixel creation using post method --------------------#
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2022, month=10, day=4)
# today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometer did you cycle today?")
    # "quantity": input("How much calory did you gain today?")

}
# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)


# ------------------- update endpoint -------------------- #
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "9.8"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)


# -------------------- Delete Pixel ------------------ #
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
