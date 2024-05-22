from flask import Blueprint, request, jsonify
from models.user_model import User
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from views.user_view import render_user_detail, render_user_list
from utils.decorators import role_required, jwt_required

user = Blueprint("user", __name__)

@user.route("/users", methods=["GET"])
#@role_required(role=["admin", "user"])
@jwt_required
def get_users():
    users = User.get_all()
    return jsonify(render_user_list(users))

@user.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    role = data.get("role")

    if not username or not password:
        return jsonify({"error": "Se requieren nombre de usuario y contraseña"}), 400

    existing_user = User.find_by_username(username)
    if existing_user:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

    new_user = User(username, password,role)
    new_user.save()

    return jsonify({"message": "Usuario creado exitosamente"}), 201


@user.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    user = User.find_by_username(username)
    if user and check_password_hash(user.password_hash, password):
        # Si las credenciales son válidas, genera un token JWT
        access_token = create_access_token(identity={"username":username,"role":user.role})
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
    
    
@user.route("/users/<int:id>", methods=["PUT"])
@role_required(role=["admin"])
@jwt_required
def update_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({"error": "Dulce no encontrado"}), 404
    data = request.json 
    
    username = data.get("username")
    password_hash = data.get("password_hash")
    role = data.get("role")
    
    user.update(username=username, password_hash=password_hash, role=role)
    
    return jsonify(render_user_detail(user))

# Ruta para eliminar un dulce existente por su ID
@user.route("/users/<int:id>", methods=["DELETE"])
@role_required(role=["admin"])
@jwt_required
def delete_user(id):
    user = User.get_by_id(id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    
    user.delete()
    return "", 204