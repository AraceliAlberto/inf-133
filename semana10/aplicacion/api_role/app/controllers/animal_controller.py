from flask import Blueprint, request, jsonify
from models.animal_model import Animal
from views.animal_view import render_animal_list, render_animal_detail
from utils.decorators import jwt_required, role_required

animal_bp = Blueprint("animal", __name__)

@animal_bp.route("/animals", methods=["GET"])
@jwt_required
@role_required(role=["admin","user"])
def get_animals():
    animals = Animal.get_all()
    return jsonify(render_animal_list(animals))

@animal_bp.route("/animals/<int:id>", methods=["GET"])
@jwt_required
@role_required(role=["admin","user"])
def get_animal(id):
    animal = Animal.get_by_id(id)
    if animal:
        return jsonify(render_animal_detail(animal))
    return jsonify({"error": "Animal no encontrado"}), 404

@animal_bp.route("/animals", methods=["POST"])
@jwt_required
@role_required(role=["admin"])
def create_animal():
    data = request.json
    name = data.get("name")
    species = data.get("species")

    if not name or not species:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    animal = Animal(name=name, species=species)
    animal.save()
    return jsonify(render_animal_detail(animal)), 201

@animal_bp.route("/animals/<int:id>", methods=["PUT"])
@jwt_required
@role_required(role=["admin"])
def update_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    data = request.json
    name = data.get("name")
    species = data.get("species")

    animal.update(name=name, species=species)
    return jsonify(render_animal_detail(animal))

@animal_bp.route("/animals/<int:id>", methods=["DELETE"])
@jwt_required
@role_required(role=["admin"])
def delete_animal(id):
    animal = Animal.get_by_id(id)

    if not animal:
        return jsonify({"error": "Animal no encontrado"}), 404

    animal.delete()
    return "", 204