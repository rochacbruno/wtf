News App da parte 4 (e5) do artigo What the Flask - Introdução ao desenvolvimento web com Python e Flask

Para mais informações acesse [http://pythonclub.com.br/tag/what-the-flask.html](http://pythonclub.com.br/tag/what-the-flask.html)

Esta versão é a versão final da parte 4 "What the Flask? pt 4 e 5 Criando Extensões para o Flask" onde criamos a extensão `SimpleSitemap` e nesta branch a extensão é adicionada ao CMS

O código da extensão se encontra em: [https://github.com/rochacbruno/flask_simple_sitemap](https://github.com/rochacbruno/flask_simple_sitemap)


# Executando o CMS

Tendo o virtualenvwrapper instalado faça o seguinte.

```bash
mkvirtualenv wtf_env
...

git clone https://github.com/rochacbruno/wtf
cd wtf
git checkout sitemap
pip install -r requirements.txt --upgrade
```

Você vai precisar do MongoDB

```bash
docker run -d -p 27017:27017 mongo
```

Para rodar os testes
```bash
make test
ou
nosetests tests/
```

para executar o CMS

```bash
python run.py
```
