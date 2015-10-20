News App da parte 3 do artigo What the Flask - Introdução ao desenvolvimento web com Python e Flask

Para mais informações acesse http://pythonclub.com.br/tag/what-the-flask.html

Esta versão é a versão final da parte 3 "What the Flask? Pt-3 Plug & Use - extensões essenciais para iniciar seu projeto" e implementa algumas das principais extensoes do Flask.

tendo o virtualenvwrapper instalado faça o seguinte.

```bash
mkvirtualenv wtf_env
...

git clone https://github.com/rochacbruno/wtf
cd wtf
git checkout extended
pip install -r requirements.txt --upgrade
```

Para rodar os testes
```bash
make test
ou
nosetests tests/
```

para rodar

```bash
python run.py
```
