import requests

#definir la consulta  #que quiero obtener entre
query = """ 
    {
        hello
    }
"""

query = """ 
    {
        goodbye
    }
"""

url = 'http://localhost:8000/graphql'

# Solicitud POST al servidor GraphQL
response = requests.post(url, json={'query': query})
print(response.text) #respuesta DICCIONARIO
