# coding: utf-8
from .db import db


class Noticia(db.Document):
    titulo = db.StringField()
    texto = db.StringField()
    imagem = db.StringField()
