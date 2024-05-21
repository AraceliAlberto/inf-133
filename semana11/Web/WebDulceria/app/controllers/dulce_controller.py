
from flask import Blueprint, request, jsonify
from models.dulce_model import dulce
from views.dulce_view import render_dulce_list, render_dulce_detail
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from functools import wraps

# Crear un blueprint para el controlador de dulcees
dulce_bp = Blueprint("dulce", __name__)


def jwt_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return fn(*args, **kwargs)
        except Exception as e:
            return jsonify({"error": str(e)}), 401

    return wrapper


# Ruta para obtener la lista de dulcees
@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required
def get_dulces():
    dulces = dulce.get_all()
    return jsonify(render_dulce_list(dulces))


# Ruta para obtener un dulce específico por su ID
@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
def get_dulce(id):
    dulce = dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "dulce no encontrado"}), 404


# Ruta para crear un nuevo dulce
@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
def create_dulce():
    data = request.json
    marca = data.get("marca")
    peso = data.get("peso")
    sabor = data.get("sabor")
    origen = data.get("origen")

    # Validación simple de datos de entrada
    if not marca or not peso or sabor or origen is None:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo dulce y guardarlo en la base de datos
    dulce = dulce(marca=marca, peso=peso, sabor=sabor, origen=origen)
    dulce.save()

    return jsonify(render_dulce_detail(dulce)), 201


# Ruta para actualizar un dulce existente
@dulce_bp.route("/dulces/<int:id>", methods=["PUT"])
@jwt_required
def update_dulce(id):
    dulce = dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "dulce no encontrado"}), 404

    data = request.json
    marca = data.get("marca")
    peso = data.get("peso")
    sabor = data.get("sabor")
    origen = data.get("origen")

    # Actualizar los datos del dulce
    dulce.update(marca=marca, peso=peso, sabor=sabor, origen=origen)

    return jsonify(render_dulce_detail(dulce))


# Ruta para eliminar un dulce existente
@dulce_bp.route("/dulces/<int:id>", methods=["DELETE"])
@jwt_required
def delete_dulce(id):
    dulce = dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "dulce no encontrado"}), 404

    # Eliminar el dulce de la base de datos
    dulce.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
