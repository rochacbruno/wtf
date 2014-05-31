# coding: utf-8
import os
from werkzeug import secure_filename
from flask import (
    Flask, request, current_app, send_from_directory, render_template
)

from db import noticias

app = Flask("wtf")

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
app.config['MEDIA_ROOT'] = os.path.join(PROJECT_ROOT, 'media_files')


@app.route("/noticias/cadastro", methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":

        dados_do_formulario = request.form.to_dict()
        imagem = request.files.get('imagem')

        if imagem:
            filename = secure_filename(imagem.filename)
            path = os.path.join(current_app.config['MEDIA_ROOT'], filename)
            imagem.save(path)
            dados_do_formulario['imagem'] = filename

        id_nova_noticia = noticias.insert(dados_do_formulario)
        return render_template('cadastro_sucesso.html',
                                id_nova_noticia=id_nova_noticia)

    return render_template('cadastro.html', title=u"Inserir nova noticia")


@app.route("/")
def index():
    todas_as_noticias = noticias.all()
    return render_template('index.html',
                           noticias=todas_as_noticias,
                           title=u"Todas as notícias")


@app.route("/noticia/<int:noticia_id>")
def noticia(noticia_id):
    noticia = noticias.find_one(id=noticia_id)
    return render_template('noticia.html', noticia=noticia)


@app.route('/media/<path:filename>')
def media(filename):
    return send_from_directory(current_app.config.get('MEDIA_ROOT'), filename)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
