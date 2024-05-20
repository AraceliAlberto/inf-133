from flask import render_template
from flask_login import current_user


# La función `list_libros` recibe una lista de
# libroes y renderiza el template `libroes.html`
def list_libros(libros):
    return render_template(
        "libros.html",
        libros=libros,
        title="Lista de libros",
        current_user=current_user,
    )


# La función `create_libro` renderiza el
# template `create_libro.html` o devuelve un JSON
# según la solicitud
def create_libro():
    return render_template(
        "create_libro.html", title="Crear libro", current_user=current_user
    )


# La función `update_libro` recibe un libro
# y renderiza el template `update_libro.html`
def update_libro(libro):
    return render_template(
        "update_libro.html",
        title="Editar libro",
        libro=libro,
        current_user=current_user,
    )