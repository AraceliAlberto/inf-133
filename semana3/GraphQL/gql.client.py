import requests
# Definir la URL del servidor GraphQL
url = 'http://localhost:8000/graphql'

# Definir la consulta GraphQL simple

query_lista = """
{
        estudiantes{
            id
            nombre
            apellido
            carrera
        }
}
"""
# Solicitud POST al servidor GraphQL
print("\nLista a todos los estudiantes\n")
response = requests.post(url, json={'query': query_lista})
print(response.text)


query_carrera = """
{
        estudiantePorCarrera(car:"Arquitectura"){
            nombre
        }
}
"""
# Solicitud POST al servidor GraphQL
print("\nLista a todos los estudiantes con carrera\n")
response = requests.post(url, json={'query': query_carrera})
print(response.text)

# Definir la consulta GraphQL con parametros
query = """
    {
        estudiantePorId(id: 2){
            nombre
        }
    }
"""

print("\nLista a todos los estudiantes por ID\n")

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text)




# Definir la consulta GraphQL para crear nuevo estudiante
query_crear = """
mutation {
        estudiante1: crearEstudiante(nombre: "Araceli", apellido: "Gomez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
        estudiante2: crearEstudiante(nombre: "Marcelo", apellido: "Gomez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
        estudiante3: crearEstudiante(nombre: "Angela", apellido: "Gomez", carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""


print("\n Crea un nuevo estudiante\n")
response_mutation = requests.post(url, json={'query': query_crear})
print("Creandoooo.........")
print(response_mutation.text)


print("\nLista a los estudiantes\n")
# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)

# Definir la consulta GraphQL para eliminar un estudiante
query_eliminar = """
mutation {
        deleteEstudiante(id: 3) {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

print("\n Elimina un estudiante\n")
response_mutation = requests.post(url, json={'query': query_eliminar})
print(response_mutation.text)


# query para modificar a los estudiantes
query_modificar = """
mutation {
    modificarEstudiante(id: 2, nombre: "Jose", apellido: "Lopez", carrera: "Antropologia") {
        estudiante {
            id
            nombre
            apellido
            carrera
        }
    }
}
"""

print("\n Modifica un estudiante\n")
response_mutation = requests.post(url, json={'query': query_modificar})
print(response_mutation.text)

print("\n Lista a todos los estudiantes\n")
# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)

query_eliminar_por_carrera = """
mutation {
        deleteEstudiantePorCarrera(carrera: "Arquitectura") {
            estudiante {
                id
                nombre
                apellido
                carrera
            }
        }
    }
"""

print("\n Elimina un estudiante\n")
response_mutation = requests.post(url, json={'query': query_eliminar_por_carrera})
print(response_mutation.text)



print("\n Lista a todos los estudiantes\n")
# Lista de todos los estudiantes
response = requests.post(url, json={'query': query_lista})
print(response.text)