import requests
url = "http://localhost:8000"

# Listar a todos los post
print("Listar los POST")
response = requests.get(f"{url}/posts")
print(response.text)

# Obtener el post 2
print("Obtener el post 2")
# Crea un nuevo post de con el titulo
# Actualizar
# Elimina el post 2
