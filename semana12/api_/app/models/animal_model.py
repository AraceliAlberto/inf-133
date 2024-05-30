import json

from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from app.database import db

class Animal(db.Model):
    __tablename__ = "animals"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    species = db.Column(db.String(100), nullable=False)

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Animal.query.all()
    
    @staticmethod
    def get_by_id(id):
        return Animal.query.get(id)
    
    def update(self, name=None, species=None):
        if name is not None:
            self.name = name
        if species is not None:
            self.species = species
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()