from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable = False)
    usuario = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable = False)
    fecha = db.Column(db.Date, nullable=False)

    def __init__(self, nombre, email, usuario, password, fecha):
        self.nombre = nombre
        self.email = email
        self.usuario = usuario
        self.set_password(password)
        self.fecha = fecha
        
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return User.query.all()

    @staticmethod
    def get_by_id(id):
        return User.query.get(id)

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_user_by_username(usuario):
        return User.query.filter_by(usuario=usuario).first()