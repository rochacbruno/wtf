from werkzeug.wsgi import DispatcherMiddleware
from news_app import create_app as create_news_app
from another_app import create_app as create_another_app

app = create_news_app(config_filename='settings.py')
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

app.run(debug=True, use_reloader=True)
