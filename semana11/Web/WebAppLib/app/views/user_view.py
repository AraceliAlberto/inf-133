from flask import render_template
from flask_login import current_user

def usuarios(users):
    return render_template("usuarios.html", users=users, title="Lista de usuarios", current_user=current_user,)

def registro():
    return render_template("registro.html", title="Registro de usuarios", current_user=current_user)

def actualizar(user):
    return render_template("actualizar.html", title="Actualizar usuario", user=user, current_user=current_user,)

def login():
    return render_template("login.html", title="Inicio de sesión", current_user=current_user)

def perfil(user):
    return render_template("profile.html", title="Perfil de usuario", user=user, current_user=current_user,)