import requests

url = "http://localhost:8000/"

# GET consulta a la ruta /lista_estudiantes
ruta_get_lista_estudiantes = url + "lista_estudiantes"
get_response_lista_estudiantes = requests.get(ruta_get_lista_estudiantes)
print("GET /lista_estudiantes:")
print(get_response_lista_estudiantes.text)
print()

# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
ruta_post_agrega_estudiante = url + "agrega_estudiante"
nuevo_estudiante = {
    "nombre": "Juanito",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronómica",
}
post_response_agrega_estudiante = requests.post(url=ruta_post_agrega_estudiante, json=nuevo_estudiante)
print("POST /agrega_estudiante:")
print(post_response_agrega_estudiante.text)
print()

# GET elimina todos los estudiantes por la ruta /eliminar_estudiante
ruta_get_eliminar_estudiante = url + "eliminar_estudiante"
eliminar_response = requests.get(ruta_get_eliminar_estudiante)
print("GET /eliminar_estudiante:")
print(eliminar_response.text)
print()

# POST agrega un nuevo estudiante por la ruta /agrega_estudiante
# (Repetido en el ejemplo original, se puede eliminar si no es necesario)
post_response_agrega_estudiante = requests.post(url=ruta_post_agrega_estudiante, json=nuevo_estudiante)
print("POST /agrega_estudiante (repetido):")
print(post_response_agrega_estudiante.text)
print()

# GET consulta a la ruta /buscar_estudiante_id/{id}
ruta_get_buscar_estudiante_id = url + "buscar_estudiante_id/1"
buscar_estudiante_id_response = requests.get(ruta_get_buscar_estudiante_id)
print("GET /buscar_estudiante_id/1:")
print(buscar_estudiante_id_response.text)
print()

# POST actualiza un estudiante por la ruta /actualizar_estudiante
ruta_post_actualizar_estudiante = url + "actualizar_estudiante"
estudiante_actualizado = {
    "id": 1,
    "nombre": "Juan",
    "apellido": "Pérez",
    "carrera": "Ingeniería Agronómica",
}
actualizar_response = requests.post(url=ruta_post_actualizar_estudiante, json=estudiante_actualizado)
print("POST /actualizar_estudiante:")
print(actualizar_response.text)
