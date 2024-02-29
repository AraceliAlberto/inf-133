from zeep import Client

client = Client('http://localhost:8000/') #instanciar cliente
result = client.service.Saludar(nombre="Araceli")
print(result)