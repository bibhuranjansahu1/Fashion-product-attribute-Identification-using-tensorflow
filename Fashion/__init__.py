from flask import Flask

def create_app(test_config= None):

    app = Flask(__name__)
    app.secret_key = 'qwerety'

    from . import urlshort
    app.register_blueprint(fashion.fashion)

    return app
