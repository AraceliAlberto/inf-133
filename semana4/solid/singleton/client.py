import requests

url = "http://localhost:8000/"

response = requests.request(method="GET", url=url + "player")
print(response.text)

response = requests.request(
    method="POST", url=url + "player/damage", json={"damage": 30}
)
print(response.text)