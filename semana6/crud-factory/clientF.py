import requests
import json

url = "http://localhost:8000/chocolates"
headers = {"Content-Type": "application/json"}

print("POST /chocolates")
new_chocolate_data = {
    "tipo_chocolate": "Tableta",
    "peso": "35g",
    "sabor": "chocolate"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "tipo_chocolate": "Bombones",
    "peso": 55,
    "sabor": "chocolate",
    "relleno": "Crema de avellanas"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())

new_chocolate_data = {
    "tipo_chocolate": "Trufas",
    "peso": 65,
    "sabor": "chocolate",
    "relleno": "naranja"
}
response = requests.post(url=url, json=new_chocolate_data, headers=headers)
print(response.json())
print("=========================")

print("\nGET /chocolates")
response = requests.get(url=url)
print(response.json())
print("=========================\n")

print("\nPUT /chocolates")
chocolate_id_to_update = 1
updated_chocolate_data = {
    "peso": 150
}
response = requests.put(f"{url}/{chocolate_id_to_update}", json=updated_chocolate_data)
print("Chocolate actualizado:", response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())
print("=========================\n")


print("\nDELETE /chocolates")
chocolate_id_to_delete = 1
response = requests.delete(f"{url}/{chocolate_id_to_delete}")
print("Chocolate eliminado:", response.json())

# GET /chocolates
response = requests.get(url=url)
print(response.json())
