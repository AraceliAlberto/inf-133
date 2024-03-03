from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def saludar(nombre):
    return "Hola, {}!".format(nombre)

# ----> Tarea de Soap <---- # cada funcion tiene que tener dispatcher

def sumar(a,b):
    return "la suma es {}".format(a+b)

def palindromo(palabra):
    palabra = palabra.lower()
    if palabra == palabra[::-1]:
        return(f"'{palabra}' es un palíndromo.")
    else:
        return(f"'{palabra}' no es un palíndromo.")

# -------------------------------

#ruta para consultar
dispatcher = SoapDispatcher(
    "ejemplo-soap-server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

#registra el servicio (hacer para cada funcion)
dispatcher.register_function(
    "Saludar",
    saludar,
    returns={"saludo": str},
    args={"nombre": str},
)

#-----> hacer esto para cada funcion
dispatcher.register_function(
    "Sumar",  #nombre con el que llama
    sumar,    
    returns={"suma":str},
    args={"a":int, "b": int}
)

dispatcher.register_function(
    "palindromo",
    palindromo,
    returns={"palindromo":str},
    args={"palabra":str}
)
#-------------------------------

#levantar el Servidor
server = HTTPServer(("0.0.0.0", 8000), SOAPHandler)
server.dispatcher = dispatcher
print("Servidor SOAP iniciado en http://localhost:8000/")
server.serve_forever()

# iniciar servidor luego client
# http son protocolos
#