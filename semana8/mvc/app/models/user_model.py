from database import db
from sqlalchemy import Date
#db model --> permite 

class User(db.Model):
    __tablename__ = 'users'
    # Define las columnas de la tabla `users`
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable = False)
    contrasenia = db.Column(db.String(50), nullable = False)
    fecha = db.Column(db.Date, nullable=False)

    # Inicializa la clase `User`
    def __init__(self, first_name, last_name, email, contrasenia, fecha):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.contrasenia = contrasenia
        self.fecha = fecha
        

    # Guarda un usuario en la base de datos importante!!
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Obtiene todos los usuarios de la base de datos (Query)
    @staticmethod
    def get_all():
        return User.query.all()