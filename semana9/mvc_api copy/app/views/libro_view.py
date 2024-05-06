def render_libro_list(libros):
    # Representa una lista de libroes como una lista de diccionarios
    return [
        {
            "id": libro.id,
            "titulo": libro.titulo,
            "autor": libro.autor,
            "edicion": libro.edicion,
            "disponibilidad": libro.disponibilidad,
        }
        for libro in libros
    ]


def render_libro_detail(libro):
    # Representa los detalles de un libro como un diccionario
    return {
        "id": libro.id,
        "titulo": libro.titulo,
        "autor": libro.autor,
        "edicion": libro.edicion,
        "disponibilidad": libro.disponibilidad,
    }