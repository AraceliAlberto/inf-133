from database import db

class Dulce(db.Model):
    __tablename__ = "dulces"

    # Define las columnas de la tabla `dulces`
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    peso = db.Column(db.Float(100), nullable=False)
    sabor = db.Column(db.String(100), nullable=False)
    origen = db.Column(db.String(100), nullable=False)

    # Inicializa la clase `Dulce`
    def __init__(self, marca, peso, sabor, origen):
        self.marca = marca
        self.peso = peso
        self.sabor = sabor
        self.origen = origen

    # Guarda un Dulce en la base de datos
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los Dulcees de la base de datos
    @staticmethod
    def get_all():
        return Dulce.query.all()

    # Obtiene un Dulce por su ID
    @staticmethod
    def get_by_id(id):
        return Dulce.query.get(id)

    # Actualiza un Dulce en la base de datos
    def update(self, marca=None, peso=None, sabor=None, origen=None):
        if marca is not None:
            self.marca = marca
        if peso is not None:
            self.peso = peso
        if sabor is not None:
            self.sabor = sabor
        if origen is not None:
            self.origen = origen
        db.session.commit()

    # Elimina un Dulce de la base de datos
    def delete(self):
        db.session.delete(self)
        db.session.commit()