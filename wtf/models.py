# coding: utf-8
from .db import db


class Noticia(db.Document):
    titulo = db.StringField(required=True)
    texto = db.StringField(required=True)
    imagem = db.StringField()
