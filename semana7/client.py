import requests

url = 'http://localhost:5000/'

# Realizar una solicitud GET al servidor Flask
response = requests.get(url)

if response.status_code == 200:
    print("Respuesta del servidor:")
    print(response.text)
else:
    print("Error al conectar con el servidor:", response.status_code)

# Método GET: Obtener un saludo proporcionando el nombre como parámetro en la URL
params = {'nombre': 'Araceli'}
response = requests.get(url+'saludar', params=params)

if response.status_code == 200:
    data = response.json()
    mensaje = data['mensaje']
    print("Respuesta del servidor (GET):", mensaje)
else:
    print("Error al conectar con el servidor (GET):", response.status_code)

# Método GET: Sumar dos números proporcionando num1 y num2 como parámetros en la URL
params = {'num1': 5, 'num2': 3}
response = requests.get(url+'sumar', params=params)

if response.status_code == 200:
    data = response.json()
    resultado = data['resultado']
    print("Respuesta del servidor (Suma):", resultado)
else:
    print("Error al conectar con el servidor (Suma):", response.status_code)

# Método GET: Verificar si una cadena es un palíndromo
params = {'cadena': 'reconocer'}
response = requests.get(url+'palindromo', params=params)

if response.status_code == 200:
    data = response.json()
    palindromo = data['palindromo']
    print("Respuesta del servidor (Palíndromo):", palindromo)
else:
    print("Error al conectar con el servidor (Palíndromo):", response.status_code)

# Método GET: Contar la cantidad de una vocal en una cadena
params = {'cadena': 'exepciones', 'vocal': 'e'}
response = requests.get(url+'contar', params=params)

if response.status_code == 200:
    data = response.json()
    cantidad = data['cantidad']
    print("Respuesta del servidor (Contar):", cantidad)
else:
    print("Error al conectar con el servidor (Contar):", response.status_code)

# Método GET: Contar la cantidad de una vocal en una cadena
