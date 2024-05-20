from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from models.animal_model import Animal
from views import animal_view
from utils.decorators import jwt_required, roles_required

# Crear un blueprint para el controlador de libroes
libro_bp = Blueprint("libro", __name__)

@animal_bp.route("/animals")
@login_required
def list_animals():
    animals = Animal.get_all()
    return animal_view.list_animals(animals)

# Ruta para crear un nuevo libro
@libro_bp.route("/libros/create", methods=["GET", "POST"])
@login_required
@role_required("admin")
def create_libro():
    if request.method == "POST":
        flash("Libro creado exitosamente", "success")
        return redirect(url_for("animal.list_animals"))
    else:
        flash("Usted no tiene permisos", 403)
        return jsonify({"message": "Unauthorized"}), 403
    return animal_view.create_animal()

# Ruta para actualizar un libro existente
@libro_bp.route("/libros/<int:id>", methods=["PUT"])
@jwt_required
@roles_required(roles=["admin"])
def update_libro(id):
    libro = libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "libro no encontrado"}), 404

    data = request.json
    titulo = data.get("titulo")
    autor = data.get("autor")
    edicion = data.get("edicion")
    disponibilidad = data.get("disponibilidad")

    # Actualizar los datos del libro
    libro.update(titulo=titulo, autor=autor, edicion=edicion, disponibilidad=disponibilidad)

    return jsonify(render_libro_detail(libro))


# Ruta para eliminar un libro existente
@libro_bp.route("/libros/<int:id>", methods=["DELETE"])
@jwt_required
@roles_required(roles=["admin"])
def delete_libro(id):
    libro = libro.get_by_id(id)

    if not libro:
        return jsonify({"error": "libro no encontrado"}), 404

    # Eliminar el libro de la base de datos
    libro.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204