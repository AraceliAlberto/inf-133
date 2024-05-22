from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False, default="user")
    email = db.Column(db.String(50), nullable = False)
    fecha = db.Column(db.Date, nullable=False)

    def __init__(self, first_name, last_name, username, password, email, fecha, role="user"):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.set_password(password)
        self.role = role
        self.email = email
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
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()
    
    def has_role(self, role):
        return self.role == role