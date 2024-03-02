from zeep import Client

client = Client('http://localhost:8000/') #instanciar cliente
result = client.service.Saludar(nombre="Araceli")

suma = client.service.sumar(a=4, b=6)
palindromo = client.service.palindromo(palabra = "oso")

print(result)