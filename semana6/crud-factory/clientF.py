import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

# POST /chocolates
new_chocolate_data = {
    "tipo_chocolate": "Tabletas",
    "peso": "35g",
    "sabor": "chocolate"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "tipo_chocolate": "Bombones",
    "peso": "55g",
    "sabor": "chocolate",
    "relleno": "limon"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "tipo_chocolate": "Trufas",
    "peso": "65kg",
    "sabor": "chocolate",
    "relleno": "naranja"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())


# GET /chocolates
response = requests.get(url=url)
print(response.json())

# PUT 
chocolate_id_to_update = 1
updated_chocolate_data = {
    "peso": "150kg"
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())

# DELETE
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /deliveries
response = requests.get(url=url)
print(response.json())