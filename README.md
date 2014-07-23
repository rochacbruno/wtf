News App da parte 2 do artigo What the Flask - Introdução ao desenvolvimento web com Python e Flask

Para mais informações acesse http://pythonclub.com.br/tag/what-the-flask.html

Esta versão é a versão final da parte 2 "Estrutura de aplicaçṍes Flask" e implementa configurações por instance_path e multiple apps com o DispatcherMiddleware.

tendo o virtualenvwrapper instalado faça o seguinte.

```bash
mkvirtualenv wtf_env
...

git clone https://github.com/rochacbruno/wtf
cd wtf
git checkout almost_perfect
pip install -r requirements.txt
```

Para rodar os testes
```bash
make test
ou
nosetests tests/
```

para rodar a versão simples use

```bash
python run.py
# ou se quiser alterar a instancia de configuraçṍes
python run.py production
```
Para rodar a versão que une 2 apps com o DispatcherMiddleware use o **multiple_run**

```bash
python multiple_run.py
```
