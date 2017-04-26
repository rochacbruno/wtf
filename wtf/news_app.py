# coding: utf-8
from os import path
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_security import Security, MongoEngineUserDatastore
from flask_debugtoolbar import DebugToolbarExtension
###############################################
# 1) importe a nossa nova extensão
from flask_simple_sitemap import SimpleSitemap

from .admin import configure_admin
from .blueprints.noticias import noticias_blueprint
from .db import db
from .security_models import User, Role
from .cache import cache
##############################################
# 2) importe o model de Noticia
from .models import Noticia


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
    DebugToolbarExtension(app)
    cache.init_app(app)

    ############################################
    # 3) Adicionane as noticias ao sitemap
    app.config['SIMPLE_SITEMAP_PATHS'] = {
        '/noticia/{0}'.format(noticia.id): {}
        for noticia in Noticia.objects.all()
    }
    
    ############################################
    # 4) Inicialize a extensão SimpleSitemap
    SimpleSitemap(app)

    return app
