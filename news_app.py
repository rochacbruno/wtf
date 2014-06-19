# coding: utf-8
from flask import Flask

from blueprints.noticias import noticias_blueprint
app = Flask("wtf")
app.config.from_object('settings')
app.register_blueprint(noticias_blueprint)
