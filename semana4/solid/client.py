import requests

url = "http://localhost:8000/"

ruta_get = url + "estudiantes"

get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

# POST agrega un nuevo estudiante por la ruta /estudiantes
print("--->POST:\n ")
ruta_post = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Any",
    "apellido": "Gomez",
    "carrera": "Medicina",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_estudiante)
print(post_response.text)

# GET filtrando por nombre con query params
print("--->GET:\n ")
ruta_get = url + "estudiantes?nombre=Araceli"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)

"""
#PUT
print("--->PUT:\n ")
ruta_put = url + "estudiantes/1"
nuevo_estudiante = {
    "nombre": "Any",
    "apellido": "Gomez",
    "carrera": "Medicina",
}
post_response = requests.request(method="PUT", url=ruta_put, json=nuevo_estudiante)
print(post_response.text)

#DELETE
print("--->DELETE:\n ")

ruta_delete = url + "estudiantes"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronomica",
}
post_response = requests.request(method="DELETE", url=ruta_delete, json=nuevo_estudiante)
print(post_response.text)
"""