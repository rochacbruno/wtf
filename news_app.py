# coding: utf-8
from flask import Flask
from blueprints.noticias import noticias_blueprint


def create_app(config_filename=None):
    app = Flask("wtf")
    if config_filename:
        app.config.from_pyfile(config_filename)

    app.register_blueprint(noticias_blueprint)

    return app