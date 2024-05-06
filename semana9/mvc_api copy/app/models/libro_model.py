from database import db


# Define la clase `libro` que hereda de `db.Model`
# `libro` representa la tabla `libros` en la base de datos
class Libro(db.Model):
    __tablename__ = "libros"

    # Define las columnas de la tabla `libros`
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100), nullable=False)
    edicion = db.Column(db.String(100), nullable=False)
    disponibilidad = db.Column(db.String(100), nullable=False)

    # Inicializa la clase `libro`
    def __init__(self, titulo, autor, edicion, disponibilidad):
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.disponibilidad = disponibilidad

    # Guarda un libro en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los libroes de la base de datos
    @staticmethod
    def get_all():
        return libro.query.all()

    # Obtiene un libro por su ID
    @staticmethod
    def get_by_id(id):
        return libro.query.get(id)

    # Actualiza un libro en la base de datos
    def update(self, titulo=None, autor=None, edicion=None, disponibilidad=None):
        if titulo is not None:
            self.titulo = titulo
        if autor is not None:
            self.autor = autor
        if edicion is not None:
            self.edicion = edicion
        if disponibilidad is not None:
            self.disponibilidad = disponibilidad
        db.session.commit()

    # Elimina un libro de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()