from news_app import create_app
app = create_app(config_filename='settings.py')
app.run(debug=True, use_reloader=True)
