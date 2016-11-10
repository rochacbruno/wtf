# coding: utf-8
from flask import Flask, current_app


def create_app(config):
    app = Flask("wtf")
    if config:
        app.config.update(**config)

    @app.route("/")
    def index():
        return "<br>".join([
            "<b>{key}</b>: {value}".format(key=key, value=value)
            for key, value in current_app.config.iteritems()
        ])

    return app
