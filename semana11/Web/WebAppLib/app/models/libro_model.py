from database import db

class Libro(db.Model):
    __tablename__ = "Libros"
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(50), nullable=False)
    autor = db.Column(db.String(100), unique=True, nullable=False)
    edicion = db.Column(db.Integer, nullable = False)
    disponibilidad = db.Column(db.Boolean(),  nullable=False)

    def __init__(self, titulo, autor, edicion, disponibilidad):
        self.titulo = titulo
        self.autor = autor
        self.edicion = edicion
        self.disponibilidad = disponibilidad

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    @staticmethod
    def get_all():
        return Libro.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Libro.query.get(id)

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
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()