from http.server import HTTPServer, BaseHTTPRequestHandler
import json

#Manejo de parametros de consulta "Query parameters"
from urllib.parse import urlparse, parse_qs

estudiantes = [
    {
        "id": 1,
        "nombre": "Araceli",
        "apellido": "Alberto",
        "carrera": "Ingeniería de Sistemas",
    },
]
#---------------------------- CLASES staticmethod
class EstudiantesService:

    @staticmethod
    def find_student(id):
        return next(
            (estudiante for estudiante in estudiantes if estudiante["id"] == id),
            None,
        )
    
    @staticmethod
    def buscar_por_nombre(nombre):
        return [
            estudiante for estudiante in estudiantes if estudiante["nombre"] == nombre
        ]
    
    @staticmethod
    def add_student(data):
        data["id"] = len(estudiantes) + 1
        estudiantes.append(data)
        return estudiantes
    
    @staticmethod
    def actualizar_estudiante(id, data):
        estudiante = EstudiantesService.find_student(id)
        if estudiante:
            estudiante.update(data)
            return estudiantes
        else:
            return None
        
    @staticmethod
    def borrar_Estudiantes(self):
        estudiantes.clear()
        return estudiantes
    
#---------------------------- CLASES Singleton
class Player:
    _instance = None
    def __new__(cls,name):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance.name = name
            cls._instance.health = 100
        return cls._instance
    
    def to_dict(self):
        return {"name": self.name, "health": self.health}
#----------------------------  
class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))
#----------------------------

class RESTRequestHandler(BaseHTTPRequestHandler):
    
    #Estructura de las respuestas
    def response_handler(self, status_code, data):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))
    
    #buscar un objeto
    def find_student(self, id, estudiantes):
        return next(
            (estudiante for estudiante in estudiantes if estudiante["id"] == id),
            None,
        )
    
    # Cuerpo de la Solicitud
    def read_data(self):
        content_length = int(self.headers["Content-Length"])
        data = self.rfile.read(content_length)
        data = json.loads(data.decode("utf-8")) 
        return data
    

    #parametros de consulta
    def do_POST(self):
        if self.path == "/estudiantes":
            data = self.read_data()
            estudiantes = EstudiantesService.add_student(data)
            HTTPResponseHandler.handle_response(self, 201, estudiantes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        if parsed_path.path == "/estudiantes":
            if "nombre" in query_params:
                nombre = query_params["nombre"][0]
                estudiantes_filtrados = EstudiantesService.buscar_por_nombre(
                    nombre
                )
                if estudiantes_filtrados != []:
                    HTTPResponseHandler.handle_response(self, 201, estudiantes_filtrados)
                else:
                    HTTPResponseHandler.handle_response(self, 204, [])
            else:
                HTTPResponseHandler.handle_response(self, 200, estudiantes)
        elif self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = EstudiantesService.find_student(id)
            if estudiante:
                HTTPResponseHandler.handle_response(self, 200, estudiantes)
            else:
                HTTPResponseHandler.handle_response(self, 204, [])

        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_PUT(self):
        if self.path.startswith("/estudiantes/"):
            id = int(self.path.split("/")[-1])
            estudiante = EstudiantesService.actualizar_estudiante(id,data)
            data = self.read_data()
            if estudiante:
                estudiante.update(data)
                HTTPResponseHandler.handle_response(self, 200, estudiantes)
            else:
                HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )

    def do_DELETE(self):
        if self.path == "/estudiantes":
            estudiantes = EstudiantesService.borrar_Estudiantes()
            HTTPResponseHandler.handle_response(self, 200, estudiantes)
        else:
            HTTPResponseHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )


# Para hacer Correr
def run_server(port=8000):
    try:
        server_address = ("", port)
        httpd = HTTPServer(server_address, RESTRequestHandler)
        print(f"Iniciando servidor web en http://localhost:{port}/")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor web")
        httpd.socket.close()


if __name__ == "__main__":
    run_server()