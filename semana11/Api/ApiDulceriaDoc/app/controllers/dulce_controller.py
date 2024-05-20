from flask import Blueprint, request, jsonify
from models.dulce_model import Dulce
from views.dulce_view import render_dulce_list, render_dulce_detail
from utils.decorators import jwt_required, role_required

dulce_bp = Blueprint("dulce", __name__)

@dulce_bp.route("/dulces", methods=["GET"])
@jwt_required
@role_required(role=["admin","user"])
def get_dulces():
    dulces = dulce.get_all()
    return jsonify(render_dulce_list(dulces))

@dulce_bp.route("/dulces/<int:id>", methods=["GET"])
@jwt_required
@role_required(role=["admin","user"])
def get_dulce(id):
    dulce = dulce.get_by_id(id)
    if dulce:
        return jsonify(render_dulce_detail(dulce))
    return jsonify({"error": "dulce no encontrado"}), 404

@dulce_bp.route("/dulces", methods=["POST"])
@jwt_required
@role_required(role=["admin"])
def create_dulce():
    data = request.json
    name = data.get("name")
    species = data.get("species")

    if not name or not species:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    dulce = dulce(name=name, species=species)
    dulce.save()
    return jsonify(render_dulce_detail(dulce)), 201

@dulce_bp.route("/dulces/<int:id>", methods=["PUT"])
@jwt_required
@role_required(role=["admin"])
def update_dulce(id):
    dulce = dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "dulce no encontrado"}), 404

    data = request.json
    name = data.get("name")
    species = data.get("species")

    dulce.update(name=name, species=species)
    return jsonify(render_dulce_detail(dulce))

@dulce_bp.route("/dulces/<int:id>", methods=["DELETE"])
@jwt_required
@role_required(role=["admin"])
def delete_dulce(id):
    dulce = dulce.get_by_id(id)

    if not dulce:
        return jsonify({"error": "dulce no encontrado"}), 404

    dulce.delete()
    return "", 204