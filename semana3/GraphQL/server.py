from http.server import HTTPServer, BaseHTTPRequestHandler
#HTTPServer -> 
#BaseHTTPRequestHandler --> resolver las solicitudes 
import json # intecambio de datos

from graphene import ObjectType, String, Int, List, Schema

#
class Query(ObjectType): # Query = Consulta
    hello = String()

    def resolve_hello(root, info):  #la misma variable!! root = el servidor, info = status
        return "Hola Andy"

class Query(ObjectType): # Query = Consulta
    goodbye = String()

    def resolve_goodbye(root, info):  #la misma variable!! root = el servidor, info = status
        return "Bye Bye"

    
Schema = Schema(query=Query)

class GraphQLRequestHandler(BaseHTTPRequestHandler):
    def response_handler(self, status, data):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_POST(self):
        if self.path == "/graphql":
            content_length = int(self.headers["Content-Length"])
            data = self.rfile.read(content_length)
            data = json.loads(data.decode("utf-8"))
            result = Schema.execute(data["query"]) #
            self.response_handler(200, result.data)
        else:
            self.response_handler(404, {"Error": "Ruta no existente"})
    #acceder a diccionario> clave valor
            
def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, GraphQLRequestHandler) #dirrecion, clase
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__": #.\server.py
    run_server()

#501 error del servidor
    