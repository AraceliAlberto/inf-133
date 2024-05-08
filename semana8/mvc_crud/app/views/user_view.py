from flask import render_template

def usuarios(users):
    return render_template("usuarios.html", users=users, title="Lista de usuarios")

def registro():
    return render_template("registro.html", title="Registro de usuarios")

def actualizar(user):
    return render_template("actualizar.html", title="Actualizar usuario", user=user)

def eliminar(user):
    return render_template("usuarios.html", title="Lista de usuarios usuario", user=user)
