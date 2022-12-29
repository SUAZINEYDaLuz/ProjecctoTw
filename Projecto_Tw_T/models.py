from flask_login import UserMixin
from . import db


class tabelalogin(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    sobrenome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


class tabelatw(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    titlu = db.Column(db.String(255), nullable=False)
    categoria = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(120), default='image.jpg')
