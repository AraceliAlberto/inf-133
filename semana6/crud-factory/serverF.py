from http.server import HTTPServer, BaseHTTPRequestHandler
import json

# Base de datos simulada de chocolates
chocolates = {}


class Fabrica_Chocolates:
    def __init__(self, tipo_chocolate, peso, sabor, relleno = None):
        self.tipo_chocolate = tipo_chocolate
        self.peso = peso
        self.sabor = sabor
        self.relleno = relleno


class Tabletas(Fabrica_Chocolates):
    def __init__(self, peso, sabor):
        super().__init__("Tableta", peso, sabor)


class Bombones(Fabrica_Chocolates):
    def __init__(self, peso, sabor, relleno):
        super().__init__("Bombones", peso, sabor, relleno)

class Trufas(Fabrica_Chocolates):
    def __init__(self, peso, sabor, relleno):
        super().__init__("Trufas", peso, sabor, relleno)


class ChocolateFactory:
    @staticmethod
    def create_chocolate(tipo_chocolate, peso, sabor, relleno = None):
        if tipo_chocolate == "Tableta":
            return Tabletas(peso, sabor)
        elif tipo_chocolate == "Bombones":
            return Bombones(peso, sabor, relleno)
        elif tipo_chocolate == "Trufas":
            return Bombones(peso, sabor, relleno)
        else:
            raise ValueError("Tipo de Chocolate no válido")


class HTTPDataHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))

    @staticmethod
    def handle_reader(handler):
        content_length = int(handler.headers["Content-Length"])
        post_data = handler.rfile.read(content_length)
        return json.loads(post_data.decode("utf-8"))


class ChocolateService:
    def __init__(self):
        self.factory = ChocolateFactory()

    def add_chocolate(self, data):
        tipo_chocolate = data.get("tipo_chocolate", None)
        peso = data.get("peso", None)
        sabor = data.get("sabor", None)
        relleno = data.get("relleno", None)

        fabrica_chocolate = self.factory.create_chocolate(
            tipo_chocolate, peso, sabor, relleno
        )

        chocolates[len(chocolates) + 1] = fabrica_chocolate
        return fabrica_chocolate

    def list_chocolates(self):
        return {index: chocolate.__dict__ for index, chocolate in chocolates.items()} #diccionario de compresion

    def update_chocolate(self, chocolate_id, data):
        if chocolate_id in chocolates:
            chocolate = chocolates[chocolate_id]
            peso = data.get("peso", None)
            sabor = data.get("sabor", None)
            relleno = data.get("relleno", None)
            if chocolate:
                chocolate.peso = peso
            if sabor:
                chocolate.sabor = sabor
            if relleno:
                chocolate.relleno = relleno
            return chocolate
        else:
            raise None

    def delete_chocolate(self, chocolate_id): #recibe el id
        if chocolate_id in chocolates: #busca el id en el diccionario
            del chocolates[chocolate_id]
            return {"message": "Chocolate eliminado"}
        else:chocolate_id
        return None


class ChocolateRequestHandler(BaseHTTPRequestHandler): #el servidor
    def __init__(self, *args, **kwargs):  #levantar el servicio
        self.fabrica_service = ChocolateService() # el servicio
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == "/chocolates":
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.fabrica_service.add_chocolate(data) #aca es el que crea
            HTTPDataHandler.handle_response(self, 201, response_data.__dict__)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_GET(self):
        if self.path == "/chocolates":
            response_data = self.fabrica_service.list_chocolates() #llamo al servicio y se lista
            HTTPDataHandler.handle_response(self, 200, response_data)
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_PUT(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1]) #existe algo despues
            data = HTTPDataHandler.handle_reader(self)
            response_data = self.fabrica_service.update_chocolate(chocolate_id, data) #el id y el cuerpo de la solicitud
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data.__dict__)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )

    def do_DELETE(self):
        if self.path.startswith("/chocolates/"):
            chocolate_id = int(self.path.split("/")[-1])
            response_data = self.fabrica_service.delete_chocolate(chocolate_id)
            if response_data:
                HTTPDataHandler.handle_response(self, 200, response_data)
            else:
                HTTPDataHandler.handle_response(
                    self, 404, {"message": "Chocolate no encontrado"}
                )
        else:
            HTTPDataHandler.handle_response(
                self, 404, {"message": "Ruta no encontrada"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, ChocolateRequestHandler) #lo que levanta
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()