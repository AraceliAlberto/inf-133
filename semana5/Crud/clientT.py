import requests

url = "http://localhost:8000/Tacos"
headers = {'Content-type': 'application/json'}

# GET /pizzas
response = requests.get(url)
print(response.json())

# POST /pizzas
print("post Taco")
mi_taco = {
    "base": "Tortilla de maíz",
    "guiso": "Carne asada",
    "toppings": ["Cebolla", "Cilantro", "Queso"],
    "salsa": "chiles asados"
}
response = requests.post(url, json=mi_taco, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# PUT /pizzas/1
print("Editar Taco/1")
edit_taco = {
    "base": "Tortilla",
    "guiso": "Carne asada",
    "toppings": ["Queso"],
    "salsa": "tomate"
}
response = requests.post(url+"1", json=edit_taco, headers=headers)
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())

# DELETE /pizzas/1
print("DELETE /pizzas/1")
response = requests.delete(url + "/1")
print(response.json())

# GET /pizzas
response = requests.get(url)
print(response.json())