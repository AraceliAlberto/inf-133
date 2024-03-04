import requests

url = "http://localhost:8000/"


ruta_estudiantes = url + "/estudiantes"
get_estudiantes = requests.get(ruta_estudiantes)
print("Listado de estudiantes:")
print(get_estudiantes.text)
print("--------------------------")

#1
ruta_carreras = url + "/carreras"
get_carreras = requests.get(ruta_carreras)
print("mostrar todas las carreras")
print(get_carreras.text)
print("-------------------------- \n")

#2
ruta_Economia = url + "/Economia"
get_economia = requests.get(ruta_Economia)
nuevo_estudiante = {
    "id": 5,
    "nombre": "Damian",
    "apellido": "Rojas",
}
post_response_economia = requests.post(url = ruta_Economia, json=nuevo_estudiante) #json = guardar (almacenar)
print("Estudiantes de economia")
print(get_economia.text)
print("-------------------------- \n")

ruta_estudiantes = url + "/estudiantes"
get_estudiantes = requests.get(ruta_estudiantes)
print("Listado General de Estudiantes:")
print(get_estudiantes.text)
