# coding: utf-8
from os import path
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_security import Security, MongoEngineUserDatastore
from .admin import configure_admin

from .blueprints.noticias import noticias_blueprint
from .db import db
from .security_models import User, Role


def create_app(mode):
    instance_path = path.join(
        path.abspath(path.dirname(__file__)), "%s_instance" % mode
    )

    app = Flask("wtf",
                instance_path=instance_path,
                instance_relative_config=True)

    app.config.from_object('wtf.default_settings')
    app.config.from_pyfile('config.cfg')

    app.config['MEDIA_ROOT'] = path.join(
        app.config.get('PROJECT_ROOT'),
        app.instance_path,
        app.config.get('MEDIA_FOLDER')
    )

    app.register_blueprint(noticias_blueprint)

    Bootstrap(app)
    db.init_app(app)
    Security(app=app, datastore=MongoEngineUserDatastore(db, User, Role))
    configure_admin(app)
    return app
