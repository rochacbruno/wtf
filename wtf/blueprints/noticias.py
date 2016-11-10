# coding: utf-8
import os
from werkzeug import secure_filename
from flask import (
    Blueprint, request, current_app, send_from_directory, render_template
)
from ..models import Noticia
from ..cache import cache
from flask_security import login_required

noticias_blueprint = Blueprint('noticias', __name__)


@noticias_blueprint.route("/noticias/cadastro", methods=["GET", "POST"])
@login_required
def cadastro():
    if request.method == "POST":
        dados_do_formulario = request.form.to_dict()
        if not all(
           [dados_do_formulario['titulo'], dados_do_formulario['texto']]
        ):
            return render_template('error.html', error=u"Campos obrigatórios")
        imagem = request.files.get('imagem')
        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_formulario['imagem'] = filename
        nova_noticia = Noticia.objects.create(**dados_do_formulario)
        # limpa o cache sempre que add nova noticia
        cache.clear()
        return render_template('cadastro_sucesso.html',
                               id_nova_noticia=nova_noticia.id)
    return render_template('cadastro.html', title=u"Inserir nova noticia")


@noticias_blueprint.route("/")
@cache.cached(timeout=300)
def index():
    todas_as_noticias = Noticia.objects.all()
    return render_template('index.html',
                           noticias=todas_as_noticias,
                           title=u"Todas as notícias")


@noticias_blueprint.route("/noticia/<noticia_id>")
def noticia(noticia_id):
    noticia_cacheada = cache.get(noticia_id)
    if noticia_cacheada:
        noticia = noticia_cacheada
    else:
        noticia = Noticia.objects.get(id=noticia_id)
        cache.set(noticia_id, noticia, timeout=300)
    return render_template('noticia.html', noticia=noticia)


@noticias_blueprint.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)
