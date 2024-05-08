from flask import Blueprint, request, redirect, url_for
from views import user_view
from models.user_model import User
from datetime import datetime

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def usuarios():
    users = User.get_all()
    return user_view.usuarios(users)

@user_bp.route("/users", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        contrasenia = request.form['contrasenia']
        fecha_str = request.form['fecha_Nacimiento']

        fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
        user = User(first_name, last_name, email, contrasenia, fecha)

        user.save()
        return redirect(url_for("user.usuarios"))

    return user_view.registro()

@user_bp.route("/users/<int:id>", methods=["GET"])
def obtener_usuario(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    return user_view.actualizar(user)


@user_bp.route("/users/<int:id>", methods=["POST"])
def actualizar(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    #obtener datos
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form['email']
    contrasenia = request.form['contrasenia']
    fecha_str = request.form['fecha_Nacimiento']

    #actualizar datos
    user.first_name = first_name
    user.last_name = last_name
    user.email = email
    user.contrasenia = contrasenia
    fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date()
    user.fecha = fecha
    user.update()
    return redirect(url_for("user.usuarios")) #redirecciona a la ruta asociada a la funcion (a la raiz html)


@user_bp.route("/users/<int:id>/eliminar", methods=["POST"])
def eliminar(id):
    user = User.get_by_id(id)
    if not user:
        return "Usuario no encontrado", 404
    user.delete()
    return redirect(url_for("user.usuarios"))