import sys
from werkzeug.wsgi import DispatcherMiddleware
from wtf.news_app import create_app as create_news_app
from wtf.another_app import create_app as create_another_app

mode = sys.argv[1] if len(sys.argv) > 1 else 'development'

app = create_news_app(mode=mode)
another_app_config = {
    "SECRET_KEY": "HELLO_FLASK",
    "AUTHOR_NAME": "Bruno Rocha @rochacbruno"
}
another_app = create_another_app(config=another_app_config)

app.wsgi_app = DispatcherMiddleware(
    app.wsgi_app,  # servido em /
    {
        '/another': another_app,
    }
)

app.run(**app.config.get_namespace('RUN_'))
