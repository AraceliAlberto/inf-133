import requests

url = "http://localhost:8000/"

ruta_estudiantes = url + "/estudiantes"
get_estudiantes = requests.get(ruta_estudiantes)
print("Listado de estudiantes:")
print(get_estudiantes.text)
print("--------------------------")