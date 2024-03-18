from http.server import HTTPServer, BaseHTTPRequestHandler
# que da el servidor http? porque se hace rest
import json #estandar de comunicacion en la web

from urllib.parse import urlparse, parse_qs

class DeliveryVehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.packages_delivered = 0

    def deliver(self):
        if self.packages_delivered < self.capacity:
            self.packages_delivered += 1
            return "Entrega realizada con exito"
        else:
            return "El vehículo ha alcanzado su capacidad máxima de entregas"


class Motorcycle(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=10)


class Drone(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=20)

class Scout(DeliveryVehicle):
    def __init__(self):
        super().__init__(capacity=5)


class DeliveryFactory:
    def create_delivery_vehicle(self, vehicle_type):
        if vehicle_type == "motorcycle":
            return Motorcycle()
        elif vehicle_type == "drone":
            return Drone()
        elif vehicle_type == "scout":
            return Drone()
        else:
            raise ValueError("Tipo de vehículo de entrega no válido")


class DeliveryRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/delivery":
            data = self.read_data()
            delivery_factory = DeliveryFactory()
            DeliveryRequestHandler.handle_response(self, 201, delivery_factory)
        else:
            DeliveryRequestHandler.handle_response(
                self, 404, {"Error": "Ruta no existente"}
            )


def main():
    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, DeliveryRequestHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()


if __name__ == "__main__":
    main()