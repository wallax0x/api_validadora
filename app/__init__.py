# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)

    # Registra as rotas que vamos criar
    from . import routes
    app.register_blueprint(routes.bp)

    return app
